"""
Repository module for the Clinic application.
Created to fix God Object/Low Cohesion code smell - extracting data management from routes.
Phase 4: Normalized appointments to store patient_id instead of full patient object.
Phase 7: Now uses domain model classes (Patient, Appointment) instead of raw dictionaries.
"""
from models import Patient, Appointment


class ClinicRepository:
    """
    Centralized repository for managing clinic data.
    Replaces global lists and provides encapsulated data operations.
    Internally uses Patient and Appointment model objects for type safety.
    """
    
    def __init__(self):
        self._patients = []  # List of Patient objects
        self._appointments = []  # List of Appointment objects
        self._next_patient_id = 1
        self._next_appointment_id = 1
    
    # ========================================
    # Patient Operations
    # ========================================
    
    def add_patient(self, name, age, phone):
        """Add a new patient and return the patient dict."""
        patient = Patient(
            id=self._next_patient_id,
            name=name,
            age=age,
            phone=phone
        )
        self._patients.append(patient)
        self._next_patient_id += 1
        return patient.to_dict()
    
    def find_patient(self, patient_id):
        """Find a patient by ID. Returns dict or None if not found."""
        for p in self._patients:
            if p.id == patient_id:
                return p.to_dict()
        return None
    
    def _find_patient_obj(self, patient_id):
        """Internal: Find patient object by ID."""
        for p in self._patients:
            if p.id == patient_id:
                return p
        return None
    
    def get_all_patients(self):
        """Return all patients as list of dicts."""
        return [p.to_dict() for p in self._patients]
    
    def update_patient(self, patient_id, name, age, phone):
        """Update patient details."""
        patient = self._find_patient_obj(patient_id)
        if patient:
            patient.name = name
            patient.age = age
            patient.phone = phone
            return patient.to_dict()
        return None
    
    def delete_patient(self, patient_id):
        """Delete a patient and their appointments (cascade delete)."""
        self._patients = [p for p in self._patients if p.id != patient_id]
        self._appointments = [a for a in self._appointments if a.patient_id != patient_id]
    
    # ========================================
    # Appointment Operations
    # ========================================
    
    def add_appointment(self, patient_id, date, description):
        """Add a new appointment storing only patient_id (normalized)."""
        appointment = Appointment(
            id=self._next_appointment_id,
            patient_id=patient_id,
            date=date,
            description=description
        )
        self._appointments.append(appointment)
        self._next_appointment_id += 1
        return appointment.to_dict()
    
    def get_all_appointments(self):
        """Return all appointments as list of dicts."""
        return [a.to_dict() for a in self._appointments]
    
    def get_appointments_with_patient_names(self, appointments=None):
        """Return appointments enriched with patient names for display."""
        if appointments is None:
            appointments = self._appointments
        enriched = []
        for a in appointments:
            patient = self._find_patient_obj(a.patient_id)
            enriched.append({
                'id': a.id,
                'patient_id': a.patient_id,
                'patient_name': patient.name if patient else 'Unknown',
                'date': a.date,
                'description': a.description
            })
        return enriched
    
    def search_appointments(self, query=None, date=None):
        """
        Search appointments by patient name and/or date.
        
        Args:
            query: Search string to match against patient name (case-insensitive)
            date: Date string to match exactly (YYYY-MM-DD format)
        
        Returns:
            List of matching appointments enriched with patient names
        """
        results = self._appointments
        
        # Filter by date if provided
        if date:
            results = [a for a in results if a.date == date]
        
        # Filter by patient name if provided
        if query:
            query_lower = query.lower()
            filtered = []
            for a in results:
                patient = self._find_patient_obj(a.patient_id)
                if patient and query_lower in patient.name.lower():
                    filtered.append(a)
            results = filtered
        
        # Return enriched results
        return self.get_appointments_with_patient_names(results)
    
    def get_appointments_as_api_format(self):
        """Return appointments formatted for API response."""
        return [a.to_dict() for a in self._appointments]


# Global repository instance
clinic = ClinicRepository()

# Seed initial data
patient1 = clinic.add_patient('Ahmed Ali', '30', '091-111-222')
patient2 = clinic.add_patient('Sara Omar', '25', '092-222-333')

# Add initial appointment using patient_id
clinic.add_appointment(patient1['id'], '2025-10-22', 'General Checkup')
