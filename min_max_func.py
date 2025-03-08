numbers = [1,23,42,76,45,12,37,18,53]

result = max(numbers), min(numbers)
print(result)
result = max(numbers) - min(numbers)
print(result)

names = ["Mehmet", "Kerem", "Kadir", "Ali", "Veli"]
result = max(names), min(names)
print(result)

result = max(names, key=lambda item: len(item)), min(names, key=lambda item: len(item))
print(result)

result1 = [n for n in names]
result2 = [len(n) for n in names]
result3 = min([len(n) for n in names])
print(result1, result2, result3)

result = max(names, key=lambda item: len(item)), min(names, key=lambda item: len(item))
print(result)

products = [
    {"name": "laptop", "price": 1200},
    {"name": "mouse", "price": 10},
    {"name": "monitor", "price": 200},
    {"name": "keyboard", "price": 50}
]

result = max(products, key=lambda item: item["price"])
print(result)
result = min(products, key=lambda item: item["price"])["name"]
print(result)


