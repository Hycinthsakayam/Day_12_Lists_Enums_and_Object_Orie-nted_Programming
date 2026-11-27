# Notes

- `PolicyStatus` keeps the status choices consistent.
- `Policy` is abstract: subclasses must provide `calculate_premium()`.
- The policy number is exposed through a property with no setter.
- Premium collection calls each object's calculation method, so it doesn't need to know the formula details.
- Adding `HomePolicy` to the collection is an example of extending behavior without editing the base or existing subclass code (Open/Closed Principle).
