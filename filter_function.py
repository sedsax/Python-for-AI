numbers = [-5, 1, 2, -7, 3, 4, -2, 5]

def is_negative(x):
    if x < 0:
        return True
    else:
        return False


result = list(filter(lambda x: x < 0, numbers)) 
print(result)
    
result = list(filter(is_negative, numbers)) # filter() returns an iterator were the items are filtered through a function to test if the item is accepted or not.
print(result)

result = list(filter(lambda x: x % 2 == 1, numbers)) 
print(result)
    
names = ["ali", "veli", "ayşe", "fatma"]
print(names)
result = list(filter(lambda x: len(x) > 3, names))
print(result)

result = list(filter(lambda x: x[0] == "a", names))
print(result)

filteredList = list(filter(lambda x: x[0] == "a", names))
result = list(map(str.capitalize, filteredList))
print(result)

users = [
    {"username": "@ali", "posts": ["post1", "post2"]},
    {"username": "@veli", "posts": ["post1"]},
    {"username": "@ayşe", "posts": ["post1", "post2", "post3", "post4"]},
    {"username": "@fatma", "posts": ["post1", "post2", "post3"]},
    {"username": "@mehmet", "posts": []}
    ]
   
filteredUsers = list(filter(lambda x: len(x["posts"]) > 2, users))
result = list(map(lambda x: x["username"], filteredUsers))
print(result)

result = [user["username"].upper() for user in users if len(user["posts"]) > 0]
print(result)