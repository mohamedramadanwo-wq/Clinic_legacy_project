from flask import Flask, request, redirect, url_for, render_template, jsonify
import datetime
app = Flask(__name__)

patients = []
appointments = []
_next_id = 1

# ========================================
# Helper Functions (Consolidated)
# ========================================

def add_patient(name, age, phone):
    """Add a new patient to the system. (Consolidated from add_patient_record and create_patient)"""
    global _next_id
    patient = {'id': _next_id, 'name': name, 'age': age, 'phone': phone, 'notes': ''}
    patients.append(patient)
    _next_id += 1
    return patient


def find_patient(patient_id):
    """Find a patient by ID. (Consolidated from find_patient and get_patient_by_id)"""
    for p in patients:
        if p['id'] == patient_id:
            return p
    return None


@app.route('/')
def index():
    return render_template('index.html', patients=patients, appointments=appointments)

@app.route('/patients')
def list_patients():
    return render_template('patients.html', patients=patients)

@app.route('/patients/add', methods=['GET','POST'])
def patient_add():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        phone = request.form.get('phone')
        # no validation, inconsistent types
        add_patient(name, age, phone)
        return redirect(url_for('list_patients'))
    return render_template('patient_add.html')

@app.route('/patients/<int:pid>/edit', methods=['GET','POST'])
def patient_edit(pid):
    p = find_patient(pid)
    if p is None:
        return "Not Found", 404
    if request.method == 'POST':
        # direct mutation, no logging
        p['name'] = request.form.get('name')
        p['age'] = request.form.get('age')
        p['phone'] = request.form.get('phone')
        return redirect(url_for('list_patients'))
    return render_template('patient_edit.html', patient=p)

@app.route('/appointments')
def list_appointments():
    
    return render_template('appointments.html', appointments=appointments)

@app.route('/appointments/create', methods=['GET','POST'])
def appointment_create():
    if request.method == 'POST':
        pid = int(request.form.get('patient_id'))
        date = request.form.get('date')
        desc = request.form.get('description')
        patient = find_patient(pid)
        if not patient:
            return "Patient not found", 400
     
        ap = {'id': len(appointments)+1, 'patient': patient, 'date': date, 'description': desc}
        appointments.append(ap)
        return redirect(url_for('list_appointments'))
    return render_template('appointment_create.html', patients=patients)

@app.route('/api/patients', methods=['GET'])
def api_get_patients():
    return jsonify(patients)

@app.route('/api/appointments', methods=['GET'])
def api_get_appointments():
    return jsonify([{'id': a['id'], 'patient_id': a['patient']['id'], 'date': a['date'], 'description': a['description']} for a in appointments])

@app.route('/del_patient/<int:pid>')
def del_patient(pid):
    global patients, appointments
    
    newp = []
    for p in patients:
        if p['id'] != pid:
            newp.append(p)
    patients = newp
    newa = []
    for a in appointments:
        if a['patient']['id'] != pid:
            newa.append(a)
    appointments = newa
    return redirect(url_for('list_patients'))


def messy_maintenance_function(x):
   
    for p in patients:
        if p['age'] == '':
            p['age'] = None

    return len(patients) + len(appointments)


add_patient('Ahmed Ali', '30', '091-111-222')
add_patient('Sara Omar', '25', '092-222-333')
appointments.append({'id': 1, 'patient': patients[0], 'date': '2025-10-22', 'description': 'General Checkup'})

if __name__ == '__main__':
    app.run(debug=True, port=5001)