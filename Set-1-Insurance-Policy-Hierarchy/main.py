from abc import ABC, abstractmethod
from enum import Enum

class PolicyStatus(Enum):
    DRAFT = "Draft"
    ACTIVE = "Active"
    LAPSED = "Lapsed"
    CANCELLED = "Cancelled"

class Policy(ABC):
    def __init__(self, number, region, status):
        if not number.strip():
            raise ValueError("Policy number cannot be empty")
        self._number = number
        self.region = region
        self.status = status

    @property
    def policy_number(self):
        return self._number

    @abstractmethod
    def calculate_premium(self):
        pass

class MotorPolicy(Policy):
    def __init__(self, number, region, status, vehicle_value):
        super().__init__(number, region, status)
        self.vehicle_value = vehicle_value

    def calculate_premium(self):
        return self.vehicle_value * 0.04

class HomePolicy(Policy):
    def __init__(self, number, region, status, insured_value):
        super().__init__(number, region, status)
        self.insured_value = insured_value

    def calculate_premium(self):
        return self.insured_value * 0.012

policies = [
    MotorPolicy("M101", "North", PolicyStatus.ACTIVE, 500000),
    MotorPolicy("M102", "South", PolicyStatus.ACTIVE, 350000),
    HomePolicy("H201", "North", PolicyStatus.ACTIVE, 2000000),
    HomePolicy("H202", "West", PolicyStatus.LAPSED, 1500000),
    MotorPolicy("M103", "West", PolicyStatus.ACTIVE, 250000),
]
# Add a new type without changing Policy or the existing policy classes.
policies.append(HomePolicy("H203", "South", PolicyStatus.ACTIVE, 1200000))

regions = sorted({p.region for p in policies})
print("MONTHLY PREMIUM COLLECTION")
print(f"{'Policy':<8} {'Region':<8} {'Status':<10} {'Premium':>12}")
print("-" * 42)
for p in policies:
    print(f"{p.policy_number:<8} {p.region:<8} {p.status.value:<10} {p.calculate_premium():>12,.2f}")
print("\nREGION TOTALS")
region_totals = {region: sum(p.calculate_premium() for p in policies if p.region == region) for region in regions}
for region, total in region_totals.items():
    print(f"{region:<8}: {total:,.2f}")
print("\nREGION / POLICY TYPE MATRIX")
print(f"{'Region':<8} {'Motor':>12} {'Home':>12} {'Row total':>12}")
print("-" * 46)
for region in regions:
    motor_total = sum(p.calculate_premium() for p in policies if p.region == region and isinstance(p, MotorPolicy))
    home_total = sum(p.calculate_premium() for p in policies if p.region == region and isinstance(p, HomePolicy))
    print(f"{region:<8} {motor_total:>12,.2f} {home_total:>12,.2f} {motor_total+home_total:>12,.2f}")
motor_grand = sum(p.calculate_premium() for p in policies if isinstance(p, MotorPolicy))
home_grand = sum(p.calculate_premium() for p in policies if isinstance(p, HomePolicy))
print(f"{'Column total':<8} {motor_grand:>12,.2f} {home_grand:>12,.2f} {motor_grand+home_grand:>12,.2f}")
