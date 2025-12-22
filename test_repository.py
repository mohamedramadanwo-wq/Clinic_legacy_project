"""
Unit Tests for Clinic Legacy Application

Run with: pytest test_repository.py -v
"""
import pytest
from repository import ClinicRepository


class TestPatientOperations:
    """Tests for patient-related repository operations."""
    
    @pytest.fixture
    def repo(self):
        """Create a fresh repository for each test."""
        return ClinicRepository()
    
    # Test 1: add_patient
    def test_add_patient_creates_patient_with_correct_data(self, repo):
        """Test that add_patient creates a patient with all required fields."""
        patient = repo.add_patient("John Doe", "30", "091-123-456")
        
        assert patient['id'] == 1
        assert patient['name'] == "John Doe"
        assert patient['age'] == "30"
        assert patient['phone'] == "091-123-456"
        assert patient['notes'] == ""
    
    # Test 2: add_patient increments ID
    def test_add_patient_increments_id(self, repo):
        """Test that each new patient gets a unique incremented ID."""
        patient1 = repo.add_patient("Patient 1", "25", "111")
        patient2 = repo.add_patient("Patient 2", "30", "222")
        patient3 = repo.add_patient("Patient 3", "35", "333")
        
        assert patient1['id'] == 1
        assert patient2['id'] == 2
        assert patient3['id'] == 3
    
    # Test 3: find_patient (existing)
    def test_find_patient_returns_correct_patient(self, repo):
        """Test that find_patient returns the correct patient by ID."""
        repo.add_patient("Alice", "28", "111")
        repo.add_patient("Bob", "35", "222")
        
        found = repo.find_patient(2)
        
        assert found is not None
        assert found['name'] == "Bob"
        assert found['id'] == 2
    
    # Test 4: find_patient (non-existing)
    def test_find_patient_returns_none_for_invalid_id(self, repo):
        """Test that find_patient returns None for non-existent patient."""
        repo.add_patient("Alice", "28", "111")
        
        found = repo.find_patient(999)
        
        assert found is None
    
    # Test 5: get_all_patients
    def test_get_all_patients_returns_all(self, repo):
        """Test that get_all_patients returns all added patients."""
        repo.add_patient("Patient 1", "25", "111")
        repo.add_patient("Patient 2", "30", "222")
        
        patients = repo.get_all_patients()
        
        assert len(patients) == 2
        assert patients[0]['name'] == "Patient 1"
        assert patients[1]['name'] == "Patient 2"
    
    # Test 6: update_patient
    def test_update_patient_modifies_data(self, repo):
        """Test that update_patient correctly updates patient data."""
        repo.add_patient("Old Name", "25", "111")
        
        updated = repo.update_patient(1, "New Name", "30", "999")
        
        assert updated['name'] == "New Name"
        assert updated['age'] == "30"
        assert updated['phone'] == "999"
    
    # Test 7: delete_patient
    def test_delete_patient_removes_patient(self, repo):
        """Test that delete_patient removes the patient from the list."""
        repo.add_patient("To Delete", "25", "111")
        repo.add_patient("To Keep", "30", "222")
        
        repo.delete_patient(1)
        
        patients = repo.get_all_patients()
        assert len(patients) == 1
        assert patients[0]['name'] == "To Keep"


class TestAppointmentOperations:
    """Tests for appointment-related repository operations."""
    
    @pytest.fixture
    def repo(self):
        """Create a fresh repository with a patient for each test."""
        repo = ClinicRepository()
        repo.add_patient("Test Patient", "30", "111")
        return repo
    
    # Test 8: add_appointment
    def test_add_appointment_creates_appointment(self, repo):
        """Test that add_appointment creates an appointment with correct data."""
        appointment = repo.add_appointment(1, "2025-12-25", "Checkup")
        
        assert appointment['id'] == 1
        assert appointment['patient_id'] == 1
        assert appointment['date'] == "2025-12-25"
        assert appointment['description'] == "Checkup"
    
    # Test 9: get_all_appointments
    def test_get_all_appointments_returns_all(self, repo):
        """Test that get_all_appointments returns all appointments."""
        repo.add_appointment(1, "2025-12-25", "Checkup 1")
        repo.add_appointment(1, "2025-12-26", "Checkup 2")
        
        appointments = repo.get_all_appointments()
        
        assert len(appointments) == 2
    
    # Test 10: get_appointments_with_patient_names
    def test_get_appointments_with_patient_names_enriches_data(self, repo):
        """Test that appointments are enriched with patient names."""
        repo.add_appointment(1, "2025-12-25", "Checkup")
        
        enriched = repo.get_appointments_with_patient_names()
        
        assert len(enriched) == 1
        assert enriched[0]['patient_name'] == "Test Patient"
        assert enriched[0]['patient_id'] == 1
    
    # Test 11: search_appointments by date
    def test_search_appointments_filters_by_date(self, repo):
        """Test that search_appointments correctly filters by date."""
        repo.add_appointment(1, "2025-12-25", "Christmas Checkup")
        repo.add_appointment(1, "2025-12-26", "Day After")
        
        results = repo.search_appointments(date="2025-12-25")
        
        assert len(results) == 1
        assert results[0]['description'] == "Christmas Checkup"
    
    # Test 12: search_appointments by patient name
    def test_search_appointments_filters_by_name(self, repo):
        """Test that search_appointments correctly filters by patient name."""
        repo.add_patient("Another Patient", "25", "222")
        repo.add_appointment(1, "2025-12-25", "First Patient Checkup")
        repo.add_appointment(2, "2025-12-25", "Second Patient Checkup")
        
        results = repo.search_appointments(query="Test")
        
        assert len(results) == 1
        assert results[0]['patient_name'] == "Test Patient"
    
    # Test 13: search_appointments case-insensitive
    def test_search_appointments_is_case_insensitive(self, repo):
        """Test that search is case-insensitive."""
        repo.add_appointment(1, "2025-12-25", "Checkup")
        
        results_lower = repo.search_appointments(query="test")
        results_upper = repo.search_appointments(query="TEST")
        
        assert len(results_lower) == 1
        assert len(results_upper) == 1
    
    # Test 14: delete_patient cascades to appointments
    def test_delete_patient_removes_appointments(self, repo):
        """Test that deleting a patient also removes their appointments."""
        repo.add_appointment(1, "2025-12-25", "Checkup")
        
        repo.delete_patient(1)
        
        appointments = repo.get_all_appointments()
        assert len(appointments) == 0


class TestEdgeCases:
    """Tests for edge cases and error handling."""
    
    @pytest.fixture
    def repo(self):
        return ClinicRepository()
    
    # Test 15: update non-existent patient
    def test_update_nonexistent_patient_returns_none(self, repo):
        """Test that updating a non-existent patient returns None."""
        result = repo.update_patient(999, "Name", "30", "111")
        assert result is None
    
    # Test 16: empty repository
    def test_empty_repository_returns_empty_lists(self, repo):
        """Test that a new repository has empty patient and appointment lists."""
        assert repo.get_all_patients() == []
        assert repo.get_all_appointments() == []
    
    # Test 17: search with no results
    def test_search_with_no_matches_returns_empty(self, repo):
        """Test that search returns empty list when no matches."""
        repo.add_patient("John", "30", "111")
        repo.add_appointment(1, "2025-12-25", "Checkup")
        
        results = repo.search_appointments(query="NonExistent")
        
        assert results == []


# Run tests if executed directly
if __name__ == "__main__":
    pytest.main([__file__, "-v"])
