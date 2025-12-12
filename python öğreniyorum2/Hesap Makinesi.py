print("HOŞ GELDİNİZ.")
print("Lütfen Kişisel Bilgilerinizi Giriniz.")
isim=input("İsminizi Giriniz: ")
Soyisim=input("Soy İsminizi Giriniz: ")
iş=input("İşini Giriniz: ")
amaç=input("Uygulamayı Kullanma Amacınız Nedir ?: ")
print("Uygulamayı Kullanmaya Başlayabilirsiniz.")

print(" ")

print("----------HESAP MAKİNESİ----------")

print(" ")
 
print("""

[1] Toplama
[2] Çıkarma
[3] Çarpma
[4] Bölme
[5] Üs Alma          
""")

seçim=input("Seçiminizi Giriniz: ")

if seçim=="1" :
    sayı1=float(input("Birinci Sayıyı Giriniz: "))
    sayı2=float(input("İkinci Sayıyı Giriniz: "))
    print("Sonuç: ",sayı1+sayı2)

elif seçim=="2" :
    sayı3=float(input("Birinci Sayıyı Giriniz: "))
    sayı4=float(input("İkinci Sayıyı Giriniz: "))
    print("Sonuç: ",sayı3-sayı4)

elif seçim=="3" :
    sayı5=float(input("Birinci Sayıyı Giriniz: "))
    sayı6=float(input("İkinci Sayıyı Giriniz: "))
    print("Sonuç: ",sayı5*sayı6)

elif seçim=="4" :
    sayı7=float(input("Birinci Sayıyı Giriniz: "))
    sayı8=float(input("İkinci Sayıyı Giriniz: "))
    print("Sonuç: ",sayı7/sayı8)

elif seçim=="5" :
    sayı9=float(input("Taban Olan Sayıyı Giriniz: "))
    sayı10=float(input("Kuvvet Olan Sayıyı Giriniz: "))
    print("Sonuç: ",sayı9**sayı10)

else :
    print("Yanlış Seçimi Yaptınız.") 
    print("İşlemi Devam Ettirmek İstiyorsanız Yeniden Seçim Yapınız.")

print(" ")
 
print("----------HESAP MAKİNESİ----------")

print(" ")  

print("-Bizi Tercih Ettiğiniz İçin Teşekkür Ederiz.")
print("-Ayda Sadece 20$ Ödeyerek Premium Üye Olabilirsiniz.Premium Üyelik Almak İsterseniz Bizlere Ulaşabilirsiniz.")

print(" ")
print(" ")