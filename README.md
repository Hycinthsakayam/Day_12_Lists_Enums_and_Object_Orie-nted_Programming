# Day 12 – Lists, Enums and OOP

Today's practice was about using a few OOP ideas together instead of keeping everything inside one long script. I worked through three small scenarios: insurance policies, vehicle rentals and hospital billing.

## What is in here?

### Set 1 – Insurance Policy Hierarchy
Enums for policy status, an abstract policy class and separate premium calculations for motor and home policies. The collection also prints totals by region and a region/type summary. I added another home policy to show how the code can be extended without changing the existing policy classes.

### Set 2 – Vehicle Rental System
Car, Bike and Van use their own late-fee rules. The Rental class connects a customer with a vehicle and calculates the rental cost. The summary prints the revenue from the sample rentals.

### Set 3 – Hospital Billing Model
Outpatient, inpatient and emergency visits calculate bills differently. Appointments connect the patient, doctor and visit, and the program walks through the nested list to print department totals.

## Folder layout

Each set has its own folder with:
- `main.py` – the program
- `output.txt` – captured console output from running it
- `NOTES.md` – a few notes on the concepts used
- `test_cases.md` – checks to try

## Run it

Python 3.10+:

```bash
python main.py
```

Run the command from the respective set folder.

## Topics practiced

`list` · `Enum` · abstract classes · inheritance · properties · polymorphism · composition · nested lists · totals and aggregation

These are practice examples with sample data, not production billing or pricing systems.
