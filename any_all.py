# all -> and operatörü gibi çalışır. Tüm elemanlar True ise True döner.
# any -> veya operatörü gibi çalışır. En az bir eleman True ise True döner.

result1 = all([True, True, True, True])

result2 = all([True, False, True, True])

result3 = any([True, False, True, True])

result4 = any([False, False, False, False])
print(result1, result2, result3, result4)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result5 = all([number % 2 == 0 for number in numbers]) # all elemanları kontrol eder. Eğer hepsi True ise True döner.
result6 = any([number % 2 == 0 for number in numbers]) # any elemanları kontrol eder. Eğer en az bir tane True varsa True döner.
print(result5, result6)

result7 = all([bool(numbers) for number in numbers]) 
result8 = any([bool(numbers) for number in numbers])
print(result7, result8)