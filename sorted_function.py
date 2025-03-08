numbers = [1,23,42,76,45,12,37,18,53]

# sorted fonksiyonu ile sıralama yapabiliriz.
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)
# sorted fonksiyonu ile sıralama yaparken orjinal listemiz değişmez.
# orjinal listemizi değiştirmek için sort fonksiyonunu kullanabiliriz.
numbers.sort()
print(numbers)
# sort fonksiyonu ile orjinal listemizi değiştirebiliriz.
# sorted fonksiyonu ile sadece sıralı bir liste alırız.

print(sorted(numbers, reverse=True))
# sorted fonksiyonu ile sıralama yaparken reverse parametresi ile ters sıralama yapabiliriz.
# reverse parametresine True verirsek sıralama ters olur.

users = [
    {"username": "samet", "tweets": ["I love cake", "I love pie"]},
    {"username": "kate", "tweets": ["I love my cat"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo_luvr", "tweets": ["dogs are the best"]},
    {"username": "guitar_gal", "tweets": []}
]

print(sorted(users, key=lambda user: user["username"]))
# sorted fonksiyonu ile dictionary içindeki verileri sıralayabiliriz.
# key parametresine lambda fonksiyonu vererek sıralama yapabiliriz.
# key parametresine verdiğimiz lambda fonksiyonu ile sıralama yaparken hangi key'e göre sıralama yapacağımızı belirleriz.
# lambda' nın anlamı şudur: lambda user: user["username"] -> user dictionary'sindeki username key'ine göre sıralama yap.

#print(sorted(users, key=len))
#print(sorted(users, key=lambda user: len(user["tweets"])))
#print(sorted(users, key=len, reverse=True))

result = list(map(lambda user: user["username"], users)) # map şu işlemi yapar: users listesindeki her bir dictionary'nin username key'ine karşılık gelen value'yi alır.
print(result)
result = list(map(lambda user: user["username"], sorted(users, key=lambda user: len(user["tweets"])))) # users listesindeki dictionary'leri tweets key'ine göre sıralar ve her bir dictionary'nin username key'ine karşılık gelen value'yi alır.
print(result)