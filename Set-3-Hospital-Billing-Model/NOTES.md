# Notes

- `VisitType` defines the visit categories.
- The abstract `Visit` class exposes a read-only patient ID and requires subclasses to implement `bill()`.
- Inpatient and emergency subclasses apply their respective additional charges.
- An appointment associates a patient, doctor and visit; this models HAS-A relationships instead of making a patient or doctor inherit from a visit.
- The nested appointment lists are traversed with a single nested loop, and the bill is calculated polymorphically.
