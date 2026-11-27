from abc import ABC, abstractmethod
from enum import Enum

class VisitType(Enum):
    OUTPATIENT = "Outpatient"
    INPATIENT = "Inpatient"
    EMERGENCY = "Emergency"

class Visit(ABC):
    def __init__(self, patient_id, base_charge):
        self._patient_id = patient_id
        self.base_charge = base_charge

    @property
    def patient_id(self):
        return self._patient_id

    @abstractmethod
    def bill(self):
        pass

class OutpatientVisit(Visit):
    def bill(self):
        return self.base_charge

class InpatientVisit(Visit):
    def bill(self):
        return self.base_charge + 1500

class EmergencyVisit(Visit):
    def bill(self):
        return self.base_charge + 1000

class Patient:
    def __init__(self, patient_id, name):
        self.patient_id = patient_id
        self.name = name

class Doctor:
    def __init__(self, doctor_id, name, department):
        self.doctor_id = doctor_id
        self.name = name
        self.department = department

class Appointment:
    # Composition: the appointment links a patient, doctor and visit.
    def __init__(self, patient, doctor, visit):
        self.patient = patient
        self.doctor = doctor
        self.visit = visit

appointments = [
    [Appointment(Patient("P101", "Anu"), Doctor("D01", "Dr. Ravi", "Cardiology"), OutpatientVisit("P101", 800)),
     Appointment(Patient("P102", "Bharat"), Doctor("D02", "Dr. Meena", "Orthopaedics"), InpatientVisit("P102", 5000))],
    [Appointment(Patient("P103", "Cathy"), Doctor("D03", "Dr. Kumar", "Neurology"), EmergencyVisit("P103", 3000)),
     Appointment(Patient("P104", "Deepak"), Doctor("D01", "Dr. Ravi", "Cardiology"), OutpatientVisit("P104", 1200))],
]
print("HOSPITAL BILL SUMMARY")
print(f"{'Patient':<10} {'Doctor':<16} {'Department':<16} {'Visit':<12} {'Bill':>10}")
print("-" * 68)
department_totals = {}
for ward in appointments:
    for appointment in ward:
        v = appointment.visit
        kind = next(t.value for t in VisitType if isinstance(v, {'Outpatient':OutpatientVisit,'Inpatient':InpatientVisit,'Emergency':EmergencyVisit}[t.value]))
        amount = v.bill()
        print(f"{appointment.patient.name:<10} {appointment.doctor.name:<16} {appointment.doctor.department:<16} {kind:<12} {amount:>10,.2f}")
        department_totals[appointment.doctor.department] = department_totals.get(appointment.doctor.department, 0) + amount
print("\nDEPARTMENT TOTALS")
for dept, total in department_totals.items():
    print(f"{dept:<16}: {total:,.2f}")
print(f"Hospital total: {sum(department_totals.values()):,.2f}")
