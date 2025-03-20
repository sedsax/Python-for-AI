# Lambda fonksiyonları ile çift ve tek sayıları ayıran algoritma


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


even_numbers = list(filter(lambda x: x % 2 == 0, numbers))


odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))


print(f"Orijinal liste: {numbers}")
print(f"Çift sayılar: {even_numbers}")
print(f"Tek sayılar: {odd_numbers}")