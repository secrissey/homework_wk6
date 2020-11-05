from faker import Faker

# Creation of faker profile helper function
def getProfile():
    fake = Faker()
    return fake.profile()

# Gather Data and Place inside of database
import os
from homework_api.models import Employee
from homework_api import db

def seedData():
    for seed_num in range(10):
        data = getProfile()
        employee = Patient(data['name'],data['sex'],data['address'],data['ssn'],data['blood_group'],data['mail'] )

        db.session.add(employee)
        db.session.commit()

seedData()