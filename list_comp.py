sayilar = []

for i in range(5):
    sayilar.append(i)

print(sayilar)

sayilar2 = [i for i in range(5)]

print(sayilar2)

sayilar3 = [i for i in range(10) if i % 2 == 0]

print(sayilar3)

sayilar4 = [i if i % 2 == 0 else i * 2 for i in range(10)]

print(sayilar4)

sayilar5 = [i for i in range(10) if i % 2 == 0 if i % 3 == 0]

print(sayilar5)

sayilar6 = [(i, j) for i in range(3) for j in range(3)]

print(sayilar6)

sayilar7 = [(i, j) for i in range(3) for j in range(3) if i != j]

print(sayilar7)

kurumlar = "BTK Akademi"

for harf in kurumlar:
    print(harf.upper())

kurumlar2 = [harf.upper() for harf in kurumlar]

print(kurumlar2)

kurumlar3 = [harf for harf in kurumlar]

print(kurumlar3)

sayilar8 = [3,4,5,6,7,8,9,22,34,45]
sonuc=[]

print(sayilar8)

for sayi in sayilar8:
    if sayi % 2 == 0:
        sonuc.append(sayi)

print(sonuc)

sonuc2 = [sayi for sayi in sayilar8 if sayi % 2 == 0]
sonuc2 = [i if i % 2 == 0 else "tekSayi" for i in sayilar8]

print(sonuc2)