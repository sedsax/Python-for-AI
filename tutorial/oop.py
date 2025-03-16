from abc import ABC, abstractmethod

# 1. Soyutlama (Abstraction)
class User(ABC):
    def __init__(self, username, email):
        self.username = username
        self.email = email

    @abstractmethod
    def get_role(self):
        pass

# 2. Miras Alma (Inheritance)
class Customer(User):
    def __init__(self, username, email, address):
        super().__init__(username, email)
        self.address = address

    def get_role(self):
        return "Customer"

class Admin(User):
    def __init__(self, username, email, permissions):
        super().__init__(username, email)
        self.permissions = permissions

    def get_role(self):
        return "Admin"

# 3. Çok Biçimlilik (Polymorphism)
def print_user_role(user):
    print(f"{user.username} is a {user.get_role()}")

# 4. Kompozisyon (Composition)
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self, customer):
        self.customer = customer
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_total(self):
        return sum(product.price for product in self.products)

# 5. Özel Metotlar (Special Methods)
    def __str__(self):
        product_list = ", ".join([product.name for product in self.products])
        return f"Order for {self.customer.username}: {product_list} (Total: ${self.calculate_total():.2f})"


# Kullanıcılar
customer = Customer("john_doe", "john@example.com", "123 Main St")
admin = Admin("admin_user", "admin@example.com", ["add_product", "delete_product"])

# Kullanıcı rolleri
print_user_role(customer)
print_user_role(admin)

# Ürünler
product1 = Product("Laptop", 1200.00)
product2 = Product("Mouse", 25.50)

# Sipariş
order = Order(customer)
order.add_product(product1)
order.add_product(product2)

# Sipariş detayları
print(order)