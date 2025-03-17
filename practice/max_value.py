#answer 1
def max_value1(a, b):
    if a > b:
        return a
    else:
        return b

num1 = int(input("Birinci sayıyı girin: "))
num2 = int(input("İkinci sayıyı girin: "))

print(f"Daha büyük değer: {max_value1(num1, num2)}")

#answer 2 -----------------------------------------------------------------------------
def max_value2(a, b):
    return max(a, b)  # Python'un kendi max() fonksiyonunu kullanıyoruz

try:
    num1 = int(input("Birinci sayıyı girin: "))
    num2 = int(input("İkinci sayıyı girin: "))

    print(f"Daha büyük değer: {max_value2(num1, num2)}")
except ValueError:
    print("Lütfen sadece tam sayı girin!")

#answer 3 -----------------------------------------------------------------------------
def max_value3(a, b):
    return a if a > b else b  # Ternary (üçlü) if kullanımı

def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Geçersiz giriş! Lütfen bir tam sayı girin.")

if __name__ == "__main__":
    num1 = get_integer("Birinci sayıyı girin: ")
    num2 = get_integer("İkinci sayıyı girin: ")

    print(f"Daha büyük değer: {max_value3(num1, num2)}")
