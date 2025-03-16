numbers = [1, 2, 3, 4, 5]
numbers_str = ["6", "7", "8", "9", "10"]
names = ["ali", "veli", "ayşe", "fatma"]
people = [
    {"name": "ali", "last name": "yılmaz"},
    {"name": "veli", "last name": "kaya"},
    {"name": "ayşe", "last name": "şahin"},
    {"name": "fatma", "last name": "demir"}
    ]

def kareAl(x):
    return x**2

result = map(kareAl, numbers) # map() returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
print(result)

result = list(map(kareAl, numbers)) 
print(result)

result = list(map(lambda x: x**2, numbers))
print(result)

result = list(map(int, numbers_str))
print(numbers_str)
print(result)

result = list(map(str.capitalize, names))
print(result)

result = list(map(lambda person: person["name"], people))
print(result)