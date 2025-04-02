class CartItem:
    #constructor
    def __init__(self, name, price, quantity):
        # instance attributes
        self.name = name
        self.price = price
        self.quantity = quantity
    
    # instance methods
    def total_price(self):
        return self.price * self.quantity
    
    
# instance of CartItem
item1 = CartItem("Laptop", 1200, 2)
item2 = CartItem("Mouse", 20, 5)
item3 = CartItem("Keyboard", 50, 1)
item4 = CartItem("Monitor", 300, 1)
item5 = CartItem("Headphones", 100, 3)
item6 = CartItem("USB Cable", 10, 10)
item7 = CartItem("HDMI Cable", 15, 4)
item8 = CartItem("Webcam", 80, 2)
item9 = CartItem("Microphone", 60, 1)
item10 = CartItem("Speaker", 150, 2)
item11 = CartItem("External Hard Drive", 100, 1)
item12 = CartItem("Graphics Card", 500, 1)
item13 = CartItem("Motherboard", 200, 1)
item14 = CartItem("Power Supply", 80, 1)
item15 = CartItem("RAM", 100, 2)
item16 = CartItem("SSD", 150, 1)
item17 = CartItem("CPU", 300, 1)
item18 = CartItem("Cooling Fan", 50, 1)
item19 = CartItem("Laptop Stand", 30, 1)
item20 = CartItem("Mouse Pad", 10, 1)
item21 = CartItem("Desk", 200, 1)
item22 = CartItem("Chair", 150, 1)
item23 = CartItem("Printer", 250, 1)
item24 = CartItem("Scanner", 200, 1)
item25 = CartItem("Router", 100, 1)
item26 = CartItem("Modem", 80, 1)
item27 = CartItem("Network Switch", 150, 1)
item28 = CartItem("Ethernet Cable", 20, 5)
item29 = CartItem("Surge Protector", 30, 1)
item30 = CartItem("Webcam Stand", 25, 1)

print(f"Item: {item1.name}, Total Price: ${item1.total_price()}")
print(f"Item: {item2.name}, Total Price: ${item2.total_price()}")
print(f"Item: {item3.name}, Total Price: ${item3.total_price()}")
print(f"Item: {item4.name}, Total Price: ${item4.total_price()}")
print(f"Item: {item5.name}, Total Price: ${item5.total_price()}")
