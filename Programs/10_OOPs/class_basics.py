# class creation
class Vehicle:
    # attributes with default values
    color = "Blue"
    petrol_or_diesle = "Petrol"
    mileage = 10

    # methods
    def start():
        print("Starting vehicle boom boom..")

# object creation
car = Vehicle()
print(car.color)

bike = Vehicle()
print(bike.color)

aeroplane = Vehicle()
print(aeroplane.mileage)
print(aeroplane.petrol_or_diesle)
