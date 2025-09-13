from db.database import Database
from fastapi import HTTPException, status
from utilities.password import Hash_Password
from utilities.data_cleaning import clean_metatdata
import json

def register_recruiter(data):
    try:
        db = Database()
        hashed_password = Hash_Password.get_password_hash(data.password)
        new_recruiter = {
            "name": data.name,
            "email": data.email,
            "contact": data.contact,
            "dob": data.dob, 
            "company_name": data.company_name,
            "experience": data.experience,
            "password": hashed_password, 
            "designation": data.designation,
            "role_id": 2  
        }
        result = db.insert_query("recruiters", new_recruiter)
        if not result:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Failed to create recruiter"
            )

        return {
            "status": "success",
            "response": "Created successfully",
            "data": result
        }

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error occurred: {e}"
        )
    
def register_candidate(data):
    try:
        db = Database()
        hashed_password = Hash_Password.get_password_hash(data.password)
        experience = clean_metatdata(data.experience)
        new_candidate = {
            "name": data.name,
            "email": data.email,
            "contact": data.contact,
            "dob": data.dob, 
            "company_name": data.company_name,
            "experience": json.dumps(experience) if experience else None,
            "password": hashed_password, 
            "designation": data.designation,
            "role_id": 3  
        }
        result = db.insert_query("candidates", new_candidate)
        if not result:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Failed to create employee"
            )

        return {
            "status": "success",
            "response": "Created successfully",
            "data": result
        }

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error occurred: {e}"
        )