# Laptop class with attributes: brand, RAM, price. 
# objects with different values.

class Laptop:
    brand = "Dell"
    RAM = "6 GB"
    price = "99000" 

laptop1 = Laptop()
laptop1.brand = "Macbook"
laptop1.RAM = "16GB"
print("Laptop1 brand:", laptop1.brand)
print("Laptop1 brand:", laptop1.RAM)

laptop2 = Laptop()
laptop2.brand = "HP"
laptop2.price = "100900"
print("Laptop2 brand:", laptop2.brand)
print("Laptop2 price:", laptop2.price)