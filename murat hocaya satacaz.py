#!/usr/bin/env python3
"""
Basit, hatasız çalışması hedeflenmiş bir ders programı (Tkinter ile GUI).
Özellikler:

Hafta içi/hafta sonu ayrımı yok; gün seçilebilir
Ders ekleme: konu, süre (dakika), başlangıç saati (isteğe bağlı)
"Kitap Okuma" seçeneği: eklenirse bir kitap okuma oturumu oluşturur
Programı kaydetme / yükleme (JSON)
Programı metin olarak dışa aktarma
Çalıştırma: Python 3.x yüklüyse dosyayı kaydedip
$ python ders_programi.py
ile çalıştırın.
"""
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
from datetime import datetime

DAYS = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]


class StudyScheduleApp:
    # HATA DÜZELTİLDİ: init -> __init__
    def __init__(self, root):
        self.root = root
        root.title("Ders Programı")
        root.geometry("800x520")
        root.resizable(False, False)

        self.data = {day: [] for day in DAYS}  # her gün için liste

        # Sol panel: form
        form = ttk.Frame(root, padding=12)
        form.place(x=10, y=10, width=350, height=500)

        ttk.Label(form, text="Ders / Etkinlik Ekle", font=(None, 14, 'bold')).pack(pady=(0, 8))

        ttk.Label(form, text="Gün:").pack(anchor='w')
        self.day_var = tk.StringVar(value=DAYS[0])
        day_menu = ttk.Combobox(form, textvariable=self.day_var, values=DAYS, state='readonly')
        day_menu.pack(fill='x', pady=4)

        ttk.Label(form, text="Başlık (örn: Matematik)").pack(anchor='w')
        self.title_entry = ttk.Entry(form)
        self.title_entry.pack(fill='x', pady=4)

        ttk.Label(form, text="Süre (dakika)").pack(anchor='w')
        self.duration_entry = ttk.Entry(form)
        self.duration_entry.pack(fill='x', pady=4)

        ttk.Label(form, text="Başlangıç saati (opsiyonel - HH:MM)").pack(anchor='w')
        self.start_entry = ttk.Entry(form)
        self.start_entry.pack(fill='x', pady=4)

        self.reading_var = tk.BooleanVar()
        ttk.Checkbutton(form, text="Kitap Okuma oturumu ekle", variable=self.reading_var).pack(anchor='w', pady=6)

        ttk.Button(form, text="Ekle", command=self.add_item).pack(fill='x', pady=(6, 4))
        ttk.Button(form, text="Seçiliyi Sil", command=self.remove_selected).pack(fill='x', pady=4)

        ttk.Separator(form).pack(fill='x', pady=8)

        ttk.Button(form, text="Kaydet (JSON)", command=self.save_json).pack(fill='x', pady=4)
        ttk.Button(form, text="Yükle (JSON)", command=self.load_json).pack(fill='x', pady=4)
        ttk.Button(form, text="Dışa Aktar (.txt)", command=self.export_txt).pack(fill='x', pady=4)

        # Sağ panel: gösterge
        right = ttk.Frame(root, padding=12)
        right.place(x=370, y=10, width=420, height=500)

        ttk.Label(right, text="Haftalık Program", font=(None, 14, 'bold')).pack()

        top_ctrl = ttk.Frame(right)
        top_ctrl.pack(fill='x', pady=6)
        ttk.Label(top_ctrl, text="Gün: ").pack(side='left')
        self.view_day_var = tk.StringVar(value=DAYS[0])
        view_day_menu = ttk.Combobox(top_ctrl, textvariable=self.view_day_var, values=DAYS, state='readonly', width=12)
        view_day_menu.pack(side='left')
        view_day_menu.bind('<<ComboboxSelected>>', lambda e: self.refresh_list())

        ttk.Button(top_ctrl, text="Hepsini Göster", command=lambda: self.refresh_list(all_days=True)).pack(side='right')

        self.listbox = tk.Listbox(right, font=(None, 10))
        self.listbox.pack(fill='both', expand=True, pady=(6, 0))

        # Başlangıçta göster
        self.refresh_list()

    def add_item(self):
        title = self.title_entry.get().strip()
        duration_txt = self.duration_entry.get().strip()
        start_txt = self.start_entry.get().strip()
        day = self.day_var.get()

        # Basit validasyon
        if not title:
            messagebox.showwarning("Eksik bilgi", "Lütfen bir başlık girin (örn: Matematik).")
            return
        try:
            duration = int(duration_txt)
            if duration <= 0:
                raise ValueError()
        except Exception:
            messagebox.showwarning("Geçersiz süre", "Süreyi pozitif bir tam sayı (dakika) olarak girin.")
            return

        start_time = None
        if start_txt:
            try:
                # Saat formatını kontrol et: HH:MM
                datetime.strptime(start_txt, "%H:%M")
                start_time = start_txt
            except ValueError:
                messagebox.showwarning("Geçersiz saat",
                                       "Başlangıç saatini HH:MM formatında girin (ör. 14:30) veya boş bırakın.")
                return

        item = {"title": title, "duration": duration, "start": start_time}
        self.data[day].append(item)

        # Eğer kitap okuma seçilmişse, otomatik bir "Kitap Okuma" oturumu ekle
        if self.reading_var.get():
            read_item = {"title": "Kitap Okuma", "duration": 30, "start": None}
            self.data[day].append(read_item)

        # Temizle
        self.title_entry.delete(0, 'end')
        self.duration_entry.delete(0, 'end')
        self.start_entry.delete(0, 'end')
        self.reading_var.set(False)

        self.refresh_list()

    def remove_selected(self):
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showinfo("Seçim yok", "Silmek için bir öğe seçin.")
            return

        idx = sel[0]
        displayed = self._get_displayed_items()

        # Seçilen öğe bir gün başlığıysa (örneğin "--- Pazartesi ---"), silmeye kalkma
        if idx >= len(displayed):
            # Bu, muhtemelen bir gün başlığı seçildiği anlamına gelir, uyarı vermeye gerek yok
            return

        day, real_index = displayed[idx]
        del self.data[day][real_index]
        self.refresh_list()

    def refresh_list(self, all_days=False):
        self.listbox.delete(0, 'end')
        displayed = []
        if all_days:
            self.view_day_var.set("")  # Gün seçimini temizle
            for day in DAYS:
                # Sadece etkinlik olan günleri göster
                if self.data[day]:
                    self.listbox.insert('end', f"--- {day} ---")
                    # Gün başlığını seçilemez yap
                    self.listbox.itemconfig('end', {'bg': 'lightgray', 'fg': 'black'})

                    for i, item in enumerate(self.data[day]):
                        line = self._format_item(item)
                        self.listbox.insert('end', f"{i + 1}. {line}")
                        displayed.append((day, i))
                else:
                    self.listbox.insert('end', f"--- {day} (Etkinlik yok) ---")
                    self.listbox.itemconfig('end', {'bg': '#f0f0f0', 'fg': 'gray'})
        else:
            day = self.view_day_var.get()
            if not self.data[day]:
                self.listbox.insert('end', f"{day} için etkinlik yok.")
            for i, item in enumerate(self.data[day]):
                self.listbox.insert('end', self._format_item(item))
                displayed.append((day, i))

        # kaydetmek için referans
        self._last_displayed = displayed

    def _get_displayed_items(self):
        return getattr(self, '_last_displayed', [])

    def _format_item(self, item):
        s = f"{item['title']} — {item['duration']} dk"
        if item['start']:
            s += f" (Başl: {item['start']})"
        return s

    def save_json(self):
        path = filedialog.asksaveasfilename(defaultextension='.json', filetypes=[('JSON', '*.json')],
                                            title='Programı kaydet')
        if not path:
            return
        try:
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, ensure_ascii=False, indent=2)
            messagebox.showinfo('Kaydedildi', f'Program {path} olarak kaydedildi.')
        except Exception as e:
            messagebox.showerror('Hata', f'Kaydederken hata: {e}')

    def load_json(self):
        path = filedialog.askopenfilename(filetypes=[('JSON', '*.json')], title='Program yükle')
        if not path:
            return
        try:
            with open(path, 'r', encoding='utf-8') as f:
                loaded = json.load(f)
            # Basit doğrulama: Yüklenen veri sözlük mü ve içindeki anahtarlar doğru günleri içeriyor mu?
            valid_data = {}
            if not isinstance(loaded, dict):
                raise ValueError('Geçersiz dosya yapısı: Kök bir sözlük değil.')

            for day in DAYS:
                # Yalnızca liste olan veya boş liste olan değerleri kabul et
                if day in loaded and isinstance(loaded[day], list):
                    valid_data[day] = loaded[day]
                else:
                    valid_data[day] = []  # Geçersiz veya eksik günleri boş liste ile başlat

            self.data = valid_data
            self.refresh_list()
            messagebox.showinfo('Yüklendi', 'Program başarıyla yüklendi.')
        except Exception as e:
            messagebox.showerror('Hata', f'Yüklerken hata: {e}')

    def export_txt(self):
        path = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text', '*.txt')],
                                            title='Metin olarak kaydet')
        if not path:
            return
        try:
            with open(path, 'w', encoding='utf-8') as f:
                f.write("Haftalık Ders Programı\n")
                f.write("=" * 25 + "\n\n")
                for day in DAYS:
                    f.write(f"--- {day} ---\n")
                    if not self.data[day]:
                        f.write("  (Etkinlik yok)\n\n")
                        continue
                    for i, item in enumerate(self.data[day]):
                        line = self._format_item(item)
                        f.write(f"  {i + 1}. {line}\n")
                    f.write('\n')
            messagebox.showinfo('Dışa aktarıldı', f'Program metin dosyası olarak kaydedildi: {path}')
        except Exception as e:
            messagebox.showerror('Hata', f'Dışa aktarırken hata: {e}')


# HATA DÜZELTİLDİ: name -> __name__
if __name__ == '__main__':
    root = tk.Tk()
    app = StudyScheduleApp(root)
    root.mainloop()