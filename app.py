"""
Clinic Legacy Application - Main Flask Routes
Refactored to use ClinicRepository for data management.
Phase 6: Added form validation with flash messages.
"""
from flask import Flask, request, redirect, url_for, render_template, jsonify, flash
from repository import clinic

app = Flask(__name__)
app.secret_key = 'clinic-legacy-secret-key-2025'  # Required for flash messages


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
    """Add a new patient with validation."""
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        age = request.form.get('age', '').strip()
        phone = request.form.get('phone', '').strip()
        
        # Validation
        errors = []
        if not name:
            errors.append('Name is required')
        if not age:
            errors.append('Age is required')
        elif not age.isdigit() or int(age) < 0 or int(age) > 150:
            errors.append('Age must be a valid number between 0 and 150')
        if not phone:
            errors.append('Phone is required')
        
        if errors:
            for error in errors:
                flash(error, 'error')
            return render_template('patient_add.html', 
                                  name=name, age=age, phone=phone)
        
        clinic.add_patient(name, age, phone)
        flash('Patient added successfully!', 'success')
        return redirect(url_for('list_patients'))
    return render_template('patient_add.html')


@app.route('/patients/<int:pid>/edit', methods=['GET', 'POST'])
def patient_edit(pid):
    """Edit an existing patient with validation."""
    patient = clinic.find_patient(pid)
    if patient is None:
        flash('Patient not found', 'error')
        return redirect(url_for('list_patients'))
    
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        age = request.form.get('age', '').strip()
        phone = request.form.get('phone', '').strip()
        
        # Validation
        errors = []
        if not name:
            errors.append('Name is required')
        if not age:
            errors.append('Age is required')
        elif not age.isdigit() or int(age) < 0 or int(age) > 150:
            errors.append('Age must be a valid number between 0 and 150')
        if not phone:
            errors.append('Phone is required')
        
        if errors:
            for error in errors:
                flash(error, 'error')
            return render_template('patient_edit.html', 
                                  patient={'id': pid, 'name': name, 'age': age, 'phone': phone})
        
        clinic.update_patient(pid, name, age, phone)
        flash('Patient updated successfully!', 'success')
        return redirect(url_for('list_patients'))
    return render_template('patient_edit.html', patient=patient)


@app.route('/del_patient/<int:pid>')
def del_patient(pid):
    """Delete a patient and their appointments."""
    clinic.delete_patient(pid)
    flash('Patient deleted successfully!', 'success')
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
    """Create a new appointment with validation."""
    if request.method == 'POST':
        patient_id = request.form.get('patient_id', '').strip()
        date = request.form.get('date', '').strip()
        description = request.form.get('description', '').strip()
        
        # Validation
        errors = []
        if not patient_id:
            errors.append('Please select a patient')
        if not date:
            errors.append('Date is required')
        if not description:
            errors.append('Description is required')
        
        if errors:
            for error in errors:
                flash(error, 'error')
            return render_template('appointment_create.html', 
                                  patients=clinic.get_all_patients(),
                                  selected_patient=patient_id,
                                  date=date,
                                  description=description)
        
        pid = int(patient_id)
        patient = clinic.find_patient(pid)
        if not patient:
            flash('Patient not found', 'error')
            return render_template('appointment_create.html', 
                                  patients=clinic.get_all_patients())
        
        clinic.add_appointment(pid, date, description)
        flash('Appointment created successfully!', 'success')
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