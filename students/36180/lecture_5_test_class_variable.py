class Smartphone:
    
    def __init__(self, brand, model, battery_capacity):
        self.brand = brand              #
        self.model = model             
        self.battery = battery_capacity 


my_phone = Smartphone("Apple", "iPhone 15", 3349)

print(f"Brand: {my_phone.brand}")
print(f"Model: {my_phone.model}")
print(f"Battery: {my_phone.battery} mAh")
