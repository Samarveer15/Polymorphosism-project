class Car:
    def fuel_type(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def max_speed(self):
        raise NotImplementedError("Subclass must implement abstract method")

class BMW(Car):
    def fuel_type(self):
        return "Petrol"

    def max_speed(self):
        return "250 km/h"

class Ferrari(Car):
    def fuel_type(self):
        return "Petrol"

    def max_speed(self):
        return "340 km/h"

def display_car_info(car):
    print(f"Fuel Type: {car.fuel_type()}")
    print(f"Max Speed: {car.max_speed()}")

bmw_car = BMW()
ferrari_car = Ferrari()

print("BMW Info:")
display_car_info(bmw_car)

print("\nFerrari Info:")
display_car_info(ferrari_car)
