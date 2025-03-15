numbers = [1,3,5,2,34,56]

result = sum(numbers)
print(result) # 101
result = sum(numbers, 10)
print(result) # 111

products = [{'name': 'item1', 'price': 100}, 
            {'name': 'item2', 'price': 200}, 
            {'name': 'item3', 'price': 300}
        ]   

sumPrice = sum(product['price'] for product in products)
print(sumPrice) # 600
numberOfProduct = len([p for p in products if p['price'] > 150])
print(numberOfProduct) # 2
result = sumPrice / numberOfProduct
print(result) # 300

result = round(3.14159) 
print(result)  # 3

result = round(3.5) 
print(result)  # 4

result = round(3.14159, 2) 
print(result)  # 3.14

result = round(3.14611, 2) 
print(result)  # 3.15