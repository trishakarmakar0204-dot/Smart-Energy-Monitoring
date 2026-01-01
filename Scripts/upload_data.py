import firebase_admin
from firebase_admin import credentials, db
import csv

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://smart-energy-campus-default-rtdb.firebaseio.com/'
})

with open('../data/energy_data.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        db.reference('energy_data').push(row)

print("Data uploaded successfully!")
