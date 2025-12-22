"""
Clinic Legacy Application - Main Flask Routes
Refactored to use ClinicRepository for data management.
"""
from flask import Flask, request, redirect, url_for, render_template, jsonify
from repository import clinic

app = Flask(__name__)


# ========================================
# Web Routes
# ========================================

@app.route('/')
def index():
    """Dashboard showing patients and appointments."""
    return render_template('index.html', 
                          patients=clinic.get_all_patients(), 
                          appointments=clinic.get_appointments_with_patient_names())


@app.route('/patients')
def list_patients():
    """List all patients."""
    return render_template('patients.html', patients=clinic.get_all_patients())


@app.route('/patients/add', methods=['GET', 'POST'])
def patient_add():
    """Add a new patient."""
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        phone = request.form.get('phone')
        clinic.add_patient(name, age, phone)
        return redirect(url_for('list_patients'))
    return render_template('patient_add.html')


@app.route('/patients/<int:pid>/edit', methods=['GET', 'POST'])
def patient_edit(pid):
    """Edit an existing patient."""
    patient = clinic.find_patient(pid)
    if patient is None:
        return "Not Found", 404
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        phone = request.form.get('phone')
        clinic.update_patient(pid, name, age, phone)
        return redirect(url_for('list_patients'))
    return render_template('patient_edit.html', patient=patient)


@app.route('/del_patient/<int:pid>')
def del_patient(pid):
    """Delete a patient and their appointments."""
    clinic.delete_patient(pid)
    return redirect(url_for('list_patients'))


# ========================================
# Appointment Routes
# ========================================

@app.route('/appointments')
def list_appointments():
    """List all appointments with optional search."""
    search_query = request.args.get('q', '').strip()
    search_date = request.args.get('date', '').strip()
    
    if search_query or search_date:
        # Use search if filters provided
        appointments = clinic.search_appointments(query=search_query, date=search_date)
    else:
        # Return all appointments
        appointments = clinic.get_appointments_with_patient_names()
    
    return render_template('appointments.html', 
                          appointments=appointments,
                          search_query=search_query,
                          search_date=search_date)


@app.route('/appointments/create', methods=['GET', 'POST'])
def appointment_create():
    """Create a new appointment."""
    if request.method == 'POST':
        pid = int(request.form.get('patient_id'))
        date = request.form.get('date')
        description = request.form.get('description')
        
        patient = clinic.find_patient(pid)
        if not patient:
            return "Patient not found", 400
        
        clinic.add_appointment(pid, date, description)  # Now uses patient_id
        return redirect(url_for('list_appointments'))
    return render_template('appointment_create.html', patients=clinic.get_all_patients())


# ========================================
# API Routes
# ========================================

@app.route('/api/patients', methods=['GET'])
def api_get_patients():
    """API endpoint: Get all patients."""
    return jsonify(clinic.get_all_patients())


@app.route('/api/appointments', methods=['GET'])
def api_get_appointments():
    """API endpoint: Get all appointments."""
    return jsonify(clinic.get_appointments_as_api_format())


# ========================================
# Main Entry Point
# ========================================

if __name__ == '__main__':
    app.run(debug=True, port=5000)