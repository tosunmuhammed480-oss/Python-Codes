print('selamün aleyküm')
print('Emre\'nin Pugu')
print("""selamün
aleyküm""")
print("Mehaba\t\t\t\tDünya")
print("Merhaba\nDünya")
mesaj = "Yeşil Pug"
print(mesaj)
mesaj1 = "Yeşil"
mesaj2 = "Pug"
print(mesaj1 + mesaj2)
print(mesaj1 +" "+ mesaj2)
print(mesaj1[1])
print(mesaj1[2])
print(mesaj1[-2])
print(mesaj1[0:4])
print(mesaj1[1:4])
print(mesaj1[::2])
print(mesaj1[::3])
print(mesaj1[::1])
print(mesaj1[::-1])
print(mesaj1.upper())
print(mesaj1)
mesaj = mesaj.upper()
print(mesaj)
mesaj = mesaj.lower()
print(mesaj)
mesaj = mesaj.capitalize()
print(mesaj)
print(mesaj.startswith("Ye"))
print(mesaj.startswith("ye"))
print(mesaj.endswith("pug"))
print(len(mesaj))
print(len(mesaj + mesaj2))
print("Yeşil" + " " + mesaj2)
print("ktal" * 10)

isim = "Ali"

yas = "20"

print("{} , {} yaşındadır".format(isim,yas))

isim1 = "Ahmet"
mesajA = "Selamlar"

print("{} , \"{}\" dedi".format(isim1,mesajA))

print(f"{isim1} {mesajA} dedi")