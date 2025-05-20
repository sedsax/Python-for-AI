sample = [20, 10, 30, 40, 50]
print(sample)

print(sample[0:3]) # [20, 10, 30]

sample.append(60)
print(sample) # [20, 10, 30, 40, 50, 60]

sample.insert(2, 5) # [20, 10, 5, 30, 40, 50, 60]
print(sample)

sample.append(5)
print(sample) # [20, 10, 5, 30, 40, 50, 60, 5]

sample.remove(5) # [20, 10, 30, 40, 50, 60, 5] ilk 5'i siler
print(sample)

sample.pop(2) # [20, 10, 40, 50, 60, 5] 2. indexi siler
print(sample)

sample.pop() # [20, 10, 40, 50, 60] son elemanı siler
print(sample)

sample.sort() # [10, 20, 40, 50, 60]
print(sample)

print(sample.index(20)) # 1. indexi döner
sample.reverse() # [60, 50, 40, 20, 10]
print(sample)

print(sample.index(20)) # 3. indexi döner
print(sample)

print(sample.count(20)) # 1 tane 20 var
sample.append(20) # [60, 50, 40, 20, 10, 20]
print(sample.count(20)) # 2 tane 20 var

sample.extend([70, 80, 90]) # [60, 50, 40, 20, 10, 20, 70, 80, 90]
print(sample)

sample2 = [7, 2, 4]
sample.extend(sample2) # [60, 50, 40, 20, 10, 20, 70, 80, 90, 7, 2, 4]
print(sample)

sample3 = sample2
sample3.append(100) # [7, 2, 4, 100]
print(sample2)
print(sample3) # [7, 2, 4, 100] sample3 ve sample2 aynı referansı gösteriyor.

sample4 = sample2.copy() # [7, 2, 4]
sample4.append(200) # [7, 2, 4, 200]
print(sample2) # [7, 2, 4] sample4 ve sample2 farklı referansı gösteriyor.
print(sample4) # [7, 2, 4, 200]

sample.clear() # [] tüm elemanları siler
print(sample)
