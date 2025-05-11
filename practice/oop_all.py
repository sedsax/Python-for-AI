from abc import ABC, abstractmethod
from datetime import datetime

# -------------------- Kullanıcı Sınıfı --------------------
class User(ABC):
    def __init__(self, username, email):
        self._username = username
        self._email = email
    
    def get_info(self):
        return f"Kullanıcı: {self._username}, E-posta: {self._email}"

    @abstractmethod
    def get_role(self):
        pass


class Customer(User):
    def __init__(self, username, email):
        super().__init__(username, email)
        self.__orders = []

    def place_order(self, order):
        self.__orders.append(order)
        print(f"{self._username} adlı müşteri sipariş verdi: {order}")

    def get_orders(self):
        return self.__orders

    def get_role(self):
        return "Müşteri"


class Admin(User):
    def __init__(self, username, email):
        super().__init__(username, email)

    def get_role(self):
        return "Yönetici"

    def add_product(self, product, catalog):
        catalog.add_product(product)
        print(f"Yönetici {self._username}, ürünü ekledi: {product}")


# -------------------- Ürün Sınıfı --------------------
class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    def get_price(self):
        return self.__price

    def __str__(self):
        return f"{self.name} - {self.__price} TL"


# -------------------- Sipariş Sınıfı --------------------
class Order:
    def __init__(self, customer, product):
        self.customer = customer
        self.product = product
        self.order_date = datetime.now()

    def __str__(self):
        return f"{self.product.name} ({self.product.get_price()} TL) - {self.order_date.strftime('%Y-%m-%d %H:%M')}"

# -------------------- Katalog Sınıfı --------------------
class Catalog:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def list_products(self):
        for idx, product in enumerate(self.__products, 1):
            print(f"{idx}. {product}")

    def get_product(self, index):
        return self.__products[index]


# -------------------- Ana Akış --------------------
if __name__ == "__main__":
    # Admin ve müşteri oluştur
    admin = Admin("admin1", "admin@example.com")
    customer = Customer("mehmet", "mehmet@gmail.com")

    # Katalog ve ürünler
    catalog = Catalog()
    product1 = Product("Kulaklık", 250)
    product2 = Product("Klavye", 400)

    # Ürünleri admin ekliyor
    admin.add_product(product1, catalog)
    admin.add_product(product2, catalog)

    print("\nÜrün Kataloğu:")
    catalog.list_products()

    # Müşteri ürün satın alıyor
    selected_product = catalog.get_product(0)
    order = Order(customer, selected_product)
    customer.place_order(order)

    print("\nSiparişler:")
    for o in customer.get_orders():
        print(o)

    print("\nKullanıcı Bilgisi ve Rol:")
    print(customer.get_info())
    print("Rol:", customer.get_role())
