"""

== --> Eşit ise kontrolü yapacaktır.
if --> Eğer
"""
x=input("2024-2025 Eğitim Öğretim Yılı Yıl Sonu Ortalamanızı Giriniz: ")
x=float(x)
 

if x>=50:
        print("Bir Üst Sınıfa Geçtiniz.")

        if 50<x<85:
            print("Teşekkür Belgesi Aldınız.") 

        if 85<=x<98 :
            print("Takdir Belgesi ALdınız.")

        if  98<=x<=100:
            print("Takdir Belgesi ve Onur Belgesi Aldınız.")

elif 20<x<50:
            print("Sınıfta Kaldınız.")

else:
    print("Bir Üst Sınıfa Geçemediniz.")


   # float ondalıklar içindir.#