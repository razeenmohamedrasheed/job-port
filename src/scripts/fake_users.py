from faker import Faker
from dotenv import load_dotenv
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utilities.password import Hash_Password
import psycopg2
import random
import os
import json
from datetime import datetime

# Load env
load_dotenv()
fake = Faker()

# HR and Tech designations
hr_designations = ["HR Executive", "HR Manager", "Senior HR", "Talent Acquisition", "Recruitment Specialist"]
tech_designations = ["Software Engineer", "Senior Software Engineer", "Consultant", "Full Stack Developer",
                     "Backend Engineer", "Frontend Engineer", "AI Engineer", "Data Scientist"]

companies = [
    "Infosys", "TCS", "Wipro", "Accenture", "Capgemini", "Cognizant", "HCL Technologies",
    "IBM", "Meta", "Google", "Microsoft", "Amazon", "Apple", "Salesforce", "Oracle",
    "Adobe", "SAP", "Uber", "Flipkart", "PayPal", "Intel", "Nvidia", "Netflix", "Dell",
    "Cisco", "HP", "Sony", "Tesla", "SpaceX", "LinkedIn", "Snapchat", "Twitter",
    "Byju's", "Swiggy", "Zomato", "Ola", "Razorpay", "Freshworks", "InfoEdge"
]

# Connect DB
conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    dbname=os.getenv("DB_NAME"),
)
cur = conn.cursor()

for _ in range(200):
    name = fake.name()
    email = fake.unique.email()
    contact = fake.msisdn()[0:10]  # 10-digit contact
    dob = fake.date_of_birth(minimum_age=22, maximum_age=45).strftime("%Y-%m-%d")
    company_name = random.choice(companies)
    password = Hash_Password.get_password_hash("user123")
    created_at = updated_at = datetime.now()

    # Randomly decide role
    role_id = random.choice([2, 3])
    if role_id == 2:
        designation = random.choice(hr_designations)
    else:
        designation = random.choice(tech_designations)

    # Experience history (just 1 random job for simplicity)
    exp_history = {
        "history": [
            {
                "company_name": random.choice(companies),
                "start_date": fake.date_between(start_date="-5y", end_date="-1y").strftime("%Y-%m-%d"),
                "end_date": None,
                "designation": designation
            }
        ]
    }

    cur.execute(
        """
        INSERT INTO users (name, email, contact, dob, company_name, experience, password, designation, role_id, created_at, updated_at)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """,
        (name, email, contact, dob, company_name, json.dumps(exp_history), password, designation, role_id, created_at, updated_at)
    )

conn.commit()
cur.close()
conn.close()

print("Inserted 200 fake users successfully 🚀")
