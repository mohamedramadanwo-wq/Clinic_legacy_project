"""
Domain models for the Clinic application.
Created to fix Primitive Obsession code smell - replacing dictionaries with proper classes.
"""


class Patient:
    """Represents a patient in the clinic system."""
    
    def __init__(self, id, name, age, phone, notes=''):
        self.id = id
        self.name = name
        self.age = age
        self.phone = phone
        self.notes = notes
    
    def to_dict(self):
        """Convert patient to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'phone': self.phone,
            'notes': self.notes
        }
    
    def __repr__(self):
        return f"Patient(id={self.id}, name='{self.name}')"


class Appointment:
    """Represents an appointment in the clinic system."""
    
    def __init__(self, id, patient_id, date, description):
        self.id = id
        self.patient_id = patient_id  # Store only ID, not full patient object
        self.date = date
        self.description = description
    
    def to_dict(self):
        """Convert appointment to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'patient_id': self.patient_id,
            'date': self.date,
            'description': self.description
        }
    
    def __repr__(self):
        return f"Appointment(id={self.id}, patient_id={self.patient_id}, date='{self.date}')"
