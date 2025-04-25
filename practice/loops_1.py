ilk_metin = "asdasfddgdhfjfdgdşfkgjdfklgşjdfklgjdfkghdfjghjklsdhajlsdhjkjhkhjjh"
ikinci_metin = "sdfsuıdoryeuıfsjkdfhdjklghjdfklruseldhfjlkdshfljskeeuf"
for s in ilk_metin:
    if not s in ikinci_metin:
        print(s, end=" ")
        #print(s)

print("\n")

for s in ikinci_metin:
    if not s in ilk_metin:
        print(s, end=" ")

print("\n")

fark = ""
for s in ikinci_metin:
    if not s in ilk_metin:
        if not s in fark:
            fark += s + " "
            
print(fark + "\n")

for s in ikinci_metin:
    if not s in ilk_metin and not s in fark: # bu şekilde and ifadesini kullanarak da yazabiliriz
        fark += s

print(fark + "\n")