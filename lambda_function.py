#lambda arguments : expression

def kareAl(x):
    return x**2

sonuc = kareAl(5)
print(sonuc)

sonuc = lambda x : x**2
print(sonuc(4))

sonuc = (lambda x: x**2 )(3)
print(sonuc)

kareAl = lambda x : x**2
sonuc = kareAl(2)
print(sonuc)

topla = lambda x, y, z : x + y + z
print(topla(5, 2, 3))

def myFunction(n):
    return lambda a : a * n

product = myFunction(3)
print(product(5))

sonuc = myFunction(2)(7)
print(sonuc)