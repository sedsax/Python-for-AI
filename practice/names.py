with open("names1.txt", encoding="utf-8") as d1:
    d1_set = set(line.strip() for line in d1)

with open("names2.txt", encoding="utf-8") as d2:
    d2_set = set(line.strip() for line in d2)

# Sadece names2.txt'de olup names1.txt'de olmayanlar
for name in d2_set - d1_set:
    print(name)


for i in d2_set:
    if i not in d1_set:
        print(i, end=" ")


d1.close()
d2.close()