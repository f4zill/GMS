from pymongo import MongoClient
from datetime import datetime
import random

client = MongoClient('mongodb://localhost:27017/')
db = client['gym_management']
members_collection = db['members']

# Sample bulk insert of 500+ members
sample_names = ["John", "Sara", "Alex", "Mira", "David", "Priya"]

for i in range(501):
    member_data = {
        'name': random.choice(sample_names) + str(i),
        'phone': f'99999{i:05}',
        'email': f'user{i}@example.com',
        'gender': random.choice(['Male', 'Female', 'Other']),
        'created_at': datetime.now()
    }
    members_collection.insert_one(member_data)

print("Inserted 500+ members")
