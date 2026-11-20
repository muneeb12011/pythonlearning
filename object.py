class Car:
    def __init__(self, model, price):
        self.model = model
        self.price = price

car1 = Car("R8", 100000)
print(car1.model)

print(car1.price)

list1 = [1, 2, 3, 4, 5, 6, 7]
list1.append(8)
print(list1)


class Bike:
    def __init__(self, model, price):
        self.model = model
        self.price = price
        
Bike1 = Bike("Duke", 20000)
print(Bike1.model)
print(Bike1.price)
