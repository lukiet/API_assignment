# Create a base Vehicle class with attributes registration_number, make, and model.

class Vehicle:
    def __init__(self, registration_number, make, model):
        self.registration_number = registration_number
        self.make = make
        self.model = model

# method to display vehicle details
    def display_vehicle(self):
        print(f"Registration number : {self.registration_number}, Make : {
              self.make}, Model : {self.model}")

# Create a Car class that inherits from the Vehicle class. The Car class should have
# an additional attribute number of seats.


class Car(Vehicle):
    def __init__(self, registration_number, make, model, number_of_seats):
        super().__init__(registration_number, make, model)
        self.number_of_seats = number_of_seats

# method to display car details
    def display_car(self):
        super().display_vehicle()
        print(f"Number of seats : {self.number_of_seats}")

# Create a Truck class that inherits from the Vehicle class. The Truck class should have
# an additional attribute cargo capacity.


class Truck(Vehicle):
    def __init__(self, registration_number, make, model, cargo_capacity):
        super().__init__(registration_number, make, model)
        self.cargo_capacity = cargo_capacity

# method to display truck details
    def display_truck(self):
        super().display_vehicle()
        print(f"Cargo capacity : {self.cargo_capacity}")

# Create a Motorcycle class that inherits from the Vehicle class. The Motorcycle class should have
# an additional attribute engine capacity.


class Motorcycle(Vehicle):
    def __init__(self, registration_number, make, model, engine_capacity):
        super().__init__(registration_number, make, model)
        self.engine_capacity = engine_capacity

# method to display motorcycle details
    def display_motorcycle(self):
        super().display_vehicle()
        print(f"Engine capacity : {self.engine_capacity}")

# a Fleet class to manage the fleet, with methods to add a vehicle, display all vehicles, and search for a vehicle by registration number.


class Fleet:
    def __init__(self):
        self.vehicles = []

# method to add a vehicle to the fleet
    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f"{vehicle.make} {vehicle.model} has been added to the fleet")

# method to display all vehicles in the fleet
    def display_vehicles(self):
        if not self.vehicles:
            print("No vehicle in the fleet")
        else:
            for vehicle in self.vehicles:
                if isinstance(vehicle, Car):
                    vehicle.display_car()
                elif isinstance(vehicle, Truck):
                    vehicle.display_truck()
                elif isinstance(vehicle, Motorcycle):
                    vehicle.display_motorcycle()
                print("\n")

# method to search for a vehicle by registration number
    def search_vehicle(self, registration_number):
        for vehicle in self.vehicles:
            if vehicle.registration_number == registration_number:
                if isinstance(vehicle, Car):
                    vehicle.display_car()
                elif isinstance(vehicle, Truck):
                    vehicle.display_truck()
                elif isinstance(vehicle, Motorcycle):
                    vehicle.display_motorcycle()
                return
        print(f"Vehicle with registration number {
              registration_number} not found in the fleet")

# Using an instance of the Fleet class to demonstrate these functionalities.


def main():
    fleet = Fleet()
    while True:
        print("Welcome to Fleet Management System")
        print("1. Add Vehicle")
        print("2. Display Vehicles")
        print("3. Search Vehicle")
        print("4. Exit")

        choice = input("Enter your choice : ")

        if choice == '1':
            vehicle_type = input(
                "Enter vehicle type (car, truck, motorcycle) : ")
            registration_number = input("Enter registration number : ")
            make = input("Enter make : ")
            model = input("Enter model : ")
            if vehicle_type == 'car':
                number_of_seats = input("Enter number of seats : ")
                vehicle = Car(registration_number, make,
                              model, number_of_seats)
            elif vehicle_type == 'truck':
                cargo_capacity = input("Enter cargo capacity : ")
                vehicle = Truck(registration_number, make,
                                model, cargo_capacity)
            elif vehicle_type == 'motorcycle':
                engine_capacity = input("Enter engine capacity : ")
                vehicle = Motorcycle(registration_number,
                                     make, model, engine_capacity)
            fleet.add_vehicle(vehicle)
        elif choice == '2':
            fleet.display_vehicles()
        elif choice == '3':
            registration_number = input(
                "Enter registration number to search : ")
            fleet.search_vehicle(registration_number)
        elif choice == '4':
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
