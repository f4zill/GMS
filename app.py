from flask import Flask, render_template, request, redirect, url_for
from bson.objectid import ObjectId
from datetime import datetime
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os

load_dotenv()

app = Flask(__name__)

MONGO_URI = os.environ.get('MONGO_URI')
client = MongoClient(MONGO_URI)
db = client['gym_management']
try:
    client.admin.command('ping')
    print("✅ Connected to MongoDB Atlas successfully.")
except Exception as e:
    print("❌ MongoDB connection failed:", e)

db = client['gym_management']

# ------------------ Collections ------------------ #
members_collection = db['members']
trainers_collection = db['trainers']
equipment_collection = db['equipment']
workout_logs_collection = db['workout_logs']
payments_collection = db['payments']

# ------------------ ROUTES ------------------ #
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

# ----- MEMBERS CRUD ----- #
@app.route('/members', methods=['GET', 'POST'])
def members():
    if request.method == 'POST':
        member_data = {
            'name': request.form['name'],
            'phone': request.form['phone'],
            'email': request.form['email'],
            'gender': request.form['gender'],
            'created_at': datetime.now()
        }
        members_collection.insert_one(member_data)
        return redirect(url_for('members'))

    data = list(members_collection.find())
    for member in data:
        member['id'] = str(member['_id'])
    return render_template('members.html', data=data)

@app.route('/edit_member/<member_id>', methods=['GET', 'POST'])
def edit_member(member_id):
    member = members_collection.find_one({'_id': ObjectId(member_id)})
    if request.method == 'POST':
        updated_data = {
            'name': request.form['name'],
            'phone': request.form['phone'],
            'email': request.form['email'],
            'gender': request.form['gender']
        }
        members_collection.update_one({'_id': ObjectId(member_id)}, {'$set': updated_data})
        return redirect(url_for('members'))
    member['id'] = str(member['_id'])
    return render_template('edit_member.html', member=member)

@app.route('/delete_member/<member_id>')
def delete_member(member_id):
    members_collection.delete_one({'_id': ObjectId(member_id)})
    return redirect(url_for('members'))

# ----- TRAINERS CRUD ----- #
@app.route('/trainers', methods=['GET', 'POST'])
def trainers():
    if request.method == 'POST':
        trainer_data = {
            'name': request.form['name'],
            'phone': request.form['phone'],
            'email': request.form['email'],
            'specialty': request.form['specialty'],
            'experience_years': int(request.form['experience_years']),
            'created_at': datetime.now()
        }
        trainers_collection.insert_one(trainer_data)
        return redirect(url_for('trainers'))

    data = list(trainers_collection.find())
    for trainer in data:
        trainer['id'] = str(trainer['_id'])
    return render_template('trainers.html', data=data)

@app.route('/edit_trainer/<trainer_id>', methods=['GET', 'POST'])
def edit_trainer(trainer_id):
    trainer = trainers_collection.find_one({'_id': ObjectId(trainer_id)})
    if request.method == 'POST':
        updated_data = {
            'name': request.form['name'],
            'phone': request.form['phone'],
            'email': request.form['email'],
            'specialty': request.form['specialty'],
            'experience_years': int(request.form['experience_years'])
        }
        trainers_collection.update_one({'_id': ObjectId(trainer_id)}, {'$set': updated_data})
        return redirect(url_for('trainers'))
    trainer['id'] = str(trainer['_id'])
    return render_template('edit_trainer.html', trainer=trainer)

@app.route('/delete_trainer/<trainer_id>')
def delete_trainer(trainer_id):
    trainers_collection.delete_one({'_id': ObjectId(trainer_id)})
    return redirect(url_for('trainers'))

# ----- EQUIPMENT CRUD ----- #
@app.route('/equipment', methods=['GET', 'POST'])
def equipment():
    if request.method == 'POST':
        equipment_data = {
            'name': request.form['name'],
            'type': request.form['type'],
            'created_at': datetime.now()
        }
        equipment_collection.insert_one(equipment_data)
        return redirect(url_for('equipment'))

    data = list(equipment_collection.find())
    for item in data:
        item['id'] = str(item['_id'])
    return render_template('equipment.html', data=data)

@app.route('/edit_equipment/<equipment_id>', methods=['GET', 'POST'])
def edit_equipment(equipment_id):
    equipment = equipment_collection.find_one({'_id': ObjectId(equipment_id)})
    if request.method == 'POST':
        updated_data = {
            'name': request.form['name'],
            'type': request.form['type']
        }
        equipment_collection.update_one({'_id': ObjectId(equipment_id)}, {'$set': updated_data})
        return redirect(url_for('equipment'))
    equipment['id'] = str(equipment['_id'])
    return render_template('edit_equipment.html', equipment=equipment)

@app.route('/delete_equipment/<equipment_id>')
def delete_equipment(equipment_id):
    equipment_collection.delete_one({'_id': ObjectId(equipment_id)})
    return redirect(url_for('equipment'))

# ----- WORKOUT LOGS CRUD ----- #
@app.route('/workout_logs', methods=['GET', 'POST'])
def workout_logs():
    if request.method == 'POST':
        workout_data = {
            'member_id': request.form['member_id'],
            'trainer_id': request.form['trainer_id'],
            'workout_date': datetime.strptime(request.form['workout_date'], '%Y-%m-%d'),
            'exercises': request.form['exercises'],
            'duration_minutes': int(request.form['duration_minutes']),
            'notes': request.form.get('notes', ''),
            'created_at': datetime.now()
        }
        workout_logs_collection.insert_one(workout_data)
        return redirect(url_for('workout_logs'))

    data = []
    logs = list(workout_logs_collection.find())
    for log in logs:
        member = members_collection.find_one({'_id': ObjectId(log['member_id'])})
        trainer = trainers_collection.find_one({'_id': ObjectId(log['trainer_id'])})
        data.append({
            'id': str(log['_id']),
            'member_name': member['name'] if member else 'Unknown',
            'trainer_name': trainer['name'] if trainer else 'Unknown',
            'workout_date': log['workout_date'].strftime('%Y-%m-%d'),
            'exercises': log['exercises'],
            'duration_minutes': log['duration_minutes'],
            'notes': log.get('notes', '')
        })

    members = list(members_collection.find())
    trainers = list(trainers_collection.find())
    return render_template('workout_logs.html', data=data, members=members, trainers=trainers)

@app.route('/edit_workout_log/<log_id>', methods=['GET', 'POST'])
def edit_workout_log(log_id):
    log = workout_logs_collection.find_one({'_id': ObjectId(log_id)})
    if request.method == 'POST':
        updated_data = {
            'member_id': request.form['member_id'],
            'trainer_id': request.form['trainer_id'],
            'workout_date': datetime.strptime(request.form['workout_date'], '%Y-%m-%d'),
            'exercises': request.form['exercises'],
            'duration_minutes': int(request.form['duration_minutes']),
            'notes': request.form.get('notes', '')
        }
        workout_logs_collection.update_one({'_id': ObjectId(log_id)}, {'$set': updated_data})
        return redirect(url_for('workout_logs'))

    members = list(members_collection.find())
    trainers = list(trainers_collection.find())
    log['id'] = str(log['_id'])
    return render_template('edit_workout_log.html', log=log, members=members, trainers=trainers)

@app.route('/delete_workout_log/<log_id>')
def delete_workout_log(log_id):
    workout_logs_collection.delete_one({'_id': ObjectId(log_id)})
    return redirect(url_for('workout_logs'))

# ----- PAYMENTS CRUD ----- #
@app.route('/payments', methods=['GET', 'POST'])
def payments():
    if request.method == 'POST':
        payment_data = {
            'member_id': request.form['member_id'],
            'amount': float(request.form['amount']),
            'payment_date': datetime.strptime(request.form['payment_date'], '%Y-%m-%d'),
            'payment_method': request.form['payment_method'],
            'description': request.form.get('description', ''),
            'created_at': datetime.now()
        }
        payments_collection.insert_one(payment_data)
        return redirect(url_for('payments'))

    data = []
    payments = list(payments_collection.find())
    for payment in payments:
        member = members_collection.find_one({'_id': ObjectId(payment['member_id'])})
        data.append({
            'id': str(payment['_id']),
            'member_name': member['name'] if member else 'Unknown',
            'amount': payment['amount'],
            'payment_date': payment['payment_date'].strftime('%Y-%m-%d'),
            'payment_method': payment['payment_method'],
            'description': payment.get('description', '')
        })

    members = list(members_collection.find())
    return render_template('payments.html', data=data, members=members)

@app.route('/edit_payment/<payment_id>', methods=['GET', 'POST'])
def edit_payment(payment_id):
    payment = payments_collection.find_one({'_id': ObjectId(payment_id)})
    if request.method == 'POST':
        updated_data = {
            'member_id': request.form['member_id'],
            'amount': float(request.form['amount']),
            'payment_date': datetime.strptime(request.form['payment_date'], '%Y-%m-%d'),
            'payment_method': request.form['payment_method'],
            'description': request.form.get('description', '')
        }
        payments_collection.update_one({'_id': ObjectId(payment_id)}, {'$set': updated_data})
        return redirect(url_for('payments'))

    members = list(members_collection.find())
    payment['id'] = str(payment['_id'])
    return render_template('edit_payment.html', payment=payment, members=members)

@app.route('/delete_payment/<payment_id>')
def delete_payment(payment_id):
    payments_collection.delete_one({'_id': ObjectId(payment_id)})
    return redirect(url_for('payments'))

# ------------------ RUN ------------------ #
if __name__ == '__main__':
    app.run(debug=True)
