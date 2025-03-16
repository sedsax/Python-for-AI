import random

#answer 1
# Çift ve tek sayı sayacı
even_count = 0
odd_count = 0

# 100 rastgele sayı üret ve tek/çift kontrolü yap
for _ in range(100):
    num = random.randint(1, 100)  # 1 ile 100 arasında rastgele sayı seç
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Sonuçları yazdır
print(f"Çift sayılar: {even_count}, Tek sayılar: {odd_count}")

#answer 2 -----------------------------------------------------------------------------
def count_even_odd(numbers):
    """Verilen sayı listesindeki çift ve tek sayıların sayısını döndürür"""
    even_count2 = sum(1 for num in numbers if num % 2 == 0)
    odd_count2 = len(numbers) - even_count2
    return even_count2, odd_count2

random_numbers = [random.randint(1, 100) for _ in range(100)]

even_count2, odd_count2 = count_even_odd(random_numbers)

print(f"Çift sayılar: {even_count2}, Tek sayılar: {odd_count2}")

#answer 3 -----------------------------------------------------------------------------
def count_even_odd(numbers):
    """Verilen liste içindeki çift ve tek sayıların sayısını döndürür"""
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    odds = list(filter(lambda x: x % 2 != 0, numbers))
    return len(evens), len(odds)

if __name__ == "__main__":
    try:
        even_count, odd_count = count_even_odd(random_numbers) # random_numbers listesi yukarıda tanımlı
        print(f"Çift sayılar: {even_count}, Tek sayılar: {odd_count}")
    except Exception as e:
        print(f"Hata oluştu: {e}")
