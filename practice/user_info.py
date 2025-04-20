# Let's start by defining a simple class with an __init__ method and some attributes.
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

    #encapsulation
    def update_age(self, new_age):
        if new_age >= 0:
            self.age = new_age
        else:
            print("Yaş negatif olamaz!")

user1 = User("Ali", 30)
user2 = User("Nino", 29)

user1.display_info()
user2.display_info()

user1.update_age(32)
user1.display_info()    

user1.update_age(-35)

#------------------------------------------------------------------
# Inheritance
class AdminUser(User):
    def __init__(self, name, age, level):
        super().__init__(name, age)
        self.level = level

    def display_info(self):
        print(f"Admin Name: {self.name}, Age: {self.age}, Level: {self.level}")

admin1 = AdminUser("Zeynep", 40, "superuser")
admin1.display_info()  


# Polimorfizm 
users = [user1, user2, admin1]
for user in users:
    user.display_info()

