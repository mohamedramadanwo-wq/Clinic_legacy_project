"""
Repository module for the Clinic application.
Created to fix God Object/Low Cohesion code smell - extracting data management from routes.
Phase 4: Normalized appointments to store patient_id instead of full patient object.
"""


class ClinicRepository:
    """
    Centralized repository for managing clinic data.
    Replaces global lists and provides encapsulated data operations.
    """
    
    def __init__(self):
        self._patients = []
        self._appointments = []
        self._next_patient_id = 1
        self._next_appointment_id = 1
    
    # ========================================
    # Patient Operations
    # ========================================
    
    def add_patient(self, name, age, phone):
        """Add a new patient and return the patient dict."""
        patient = {
            'id': self._next_patient_id,
            'name': name,
            'age': age,
            'phone': phone,
            'notes': ''
        }
        self._patients.append(patient)
        self._next_patient_id += 1
        return patient
    
    def find_patient(self, patient_id):
        """Find a patient by ID. Returns None if not found."""
        for p in self._patients:
            if p['id'] == patient_id:
                return p
        return None
    
    def get_all_patients(self):
        """Return all patients."""
        return self._patients
    
    def update_patient(self, patient_id, name, age, phone):
        """Update patient details."""
        patient = self.find_patient(patient_id)
        if patient:
            patient['name'] = name
            patient['age'] = age
            patient['phone'] = phone
        return patient
    
    def delete_patient(self, patient_id):
        """Delete a patient and their appointments (cascade delete)."""
        self._patients = [p for p in self._patients if p['id'] != patient_id]
        # Now uses patient_id instead of patient['id']
        self._appointments = [a for a in self._appointments if a['patient_id'] != patient_id]
    
    # ========================================
    # Appointment Operations
    # ========================================
    
    def add_appointment(self, patient_id, date, description):
        """Add a new appointment storing only patient_id (normalized)."""
        appointment = {
            'id': self._next_appointment_id,
            'patient_id': patient_id,  # Fixed: Now stores ID only, not full object
            'date': date,
            'description': description
        }
        self._appointments.append(appointment)
        self._next_appointment_id += 1
        return appointment
    
    def get_all_appointments(self):
        """Return all appointments."""
        return self._appointments
    
    def get_appointments_with_patient_names(self):
        """Return appointments enriched with patient names for display."""
        enriched = []
        for a in self._appointments:
            patient = self.find_patient(a['patient_id'])
            enriched.append({
                'id': a['id'],
                'patient_id': a['patient_id'],
                'patient_name': patient['name'] if patient else 'Unknown',
                'date': a['date'],
                'description': a['description']
            })
        return enriched
    
    def get_appointments_as_api_format(self):
        """Return appointments formatted for API response."""
        return [
            {
                'id': a['id'],
                'patient_id': a['patient_id'],
                'date': a['date'],
                'description': a['description']
            }
            for a in self._appointments
        ]


# Global repository instance
clinic = ClinicRepository()

# Seed initial data
patient1 = clinic.add_patient('Ahmed Ali', '30', '091-111-222')
patient2 = clinic.add_patient('Sara Omar', '25', '092-222-333')

# Add initial appointment using patient_id
clinic.add_appointment(patient1['id'], '2025-10-22', 'General Checkup')
