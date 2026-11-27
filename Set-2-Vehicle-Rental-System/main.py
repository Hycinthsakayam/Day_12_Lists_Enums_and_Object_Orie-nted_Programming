from abc import ABC, abstractmethod
from enum import Enum

class VehicleType(Enum):
    CAR = "Car"
    BIKE = "Bike"
    VAN = "Van"

class Vehicle(ABC):
    def __init__(self, registration, mileage, daily_rate):
        self._registration = registration
        self._mileage = mileage
        self.daily_rate = daily_rate

    @property
    def registration(self):
        return self._registration

    @property
    def mileage(self):
        return self._mileage

    @abstractmethod
    def late_fee(self, late_days):
        pass

class Car(Vehicle):
    def late_fee(self, late_days):
        return late_days * 500

class Bike(Vehicle):
    def late_fee(self, late_days):
        return late_days * 150

class Van(Vehicle):
    def late_fee(self, late_days):
        return late_days * 750

class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id

class Rental:
    # HAS-A relationship: a rental contains a customer and a vehicle.
    def __init__(self, customer, vehicle, days, late_days=0):
        self.customer = customer
        self.vehicle = vehicle
        self.days = days
        self.late_days = late_days

    def total(self):
        return self.days * self.vehicle.daily_rate + self.vehicle.late_fee(self.late_days)

rentals = [
    Rental(Customer("Arun", "C01"), Car("TN10AB1234", 24000, 1800), 3, 1),
    Rental(Customer("Banu", "C02"), Bike("TN22CD5678", 12000, 500), 2, 0),
    Rental(Customer("Charan", "C03"), Van("TN30EF9012", 40000, 2800), 4, 2),
    Rental(Customer("Divya", "C04"), Car("TN11GH3456", 18000, 1800), 1, 0),
]
print("VEHICLE RENTAL SUMMARY")
print(f"{'Customer':<10} {'Vehicle':<8} {'Registration':<14} {'Days':>4} {'Amount':>10}")
print("-" * 54)
for r in rentals:
    kind = next(t.value for t in VehicleType if isinstance(r.vehicle, {'Car':Car,'Bike':Bike,'Van':Van}[t.value]))
    print(f"{r.customer.name:<10} {kind:<8} {r.vehicle.registration:<14} {r.days:>4} {r.total():>10,.2f}")
print(f"Total revenue: {sum(r.total() for r in rentals):,.2f}")
