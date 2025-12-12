isim="emre"
print(f"benim adım {isim}")
sayi1 = 5
sayi2 = 3.8 # 5**100 veya 22/7 bunları yazınca işlem yapiyo

print(sayi1)
print(type(sayi1))
print(type(sayi2))

# toplama +
# çıkarma-
# çarpma  *
# bölme /
#Tamsayı bölmesi //
#Kuvvet Alma **
#Mutlak Değer abs
#Yuvarlama round
#işlem önceliği

print(16/5)
print(16//5)
print(2**6)
print(abs(-2.5))
print(22/7)     #22/7 pi oluyo (3.142857142857143)
print(round(22/7))
print(round(4.9785968))
print(round(22/7,3))

#işlem önceliği
print(3 * 5 + 6)
print(3 + 5 * 6)
print((3 + 2) * 4 + 3)

#Karşılaştırma operatörleri doğru ise True yanlışsa False diyo
#Eşittir ==
#Küçüktür <
#Büyüktür >
#Küçük eşittir <=
#Büyük Eşittir >=
#eşit değildir ! ------> != olarak yazıyon

print(3 == 3)
print(3 == 5)

a = 1
b = a
a = 5
print(b)

# String ve Integerları Birbirine Çevirme
abc1 = '100'
abc2 = 100
abc3 = int(abc1)
print(type(abc1))
print(type(abc2))
print(abc1 == abc2)
print(abc3 == abc2)

abc4 = int(3.9)
print(abc4)  #bu float olduğu için tam kısmını alıyo

klm1 = 123
klm2 = str(klm1)
print(klm2)
print(klm1)
print(type(klm2))

i = 3

i = i + 5 #veya i += 5,  i *= 5 yaparsanda çarpıyo (/=) (//=)

print(i)