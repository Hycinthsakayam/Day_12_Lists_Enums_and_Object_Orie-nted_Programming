# Notes

- `VehicleType` represents the supported rental types.
- `Vehicle` is abstract and asks each concrete vehicle for its late-fee rule.
- Registration and mileage are exposed through read-only properties.
- `Rental` has a `Customer` and a `Vehicle` rather than inheriting from either; this is composition / HAS-A.
- The total is calculated in the rental class and revenue is summed in one loop.
- Keeping customer, rental and vehicle responsibilities separate avoids the original all-in-one (God) class design.
