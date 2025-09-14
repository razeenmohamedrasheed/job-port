from db.database import Database
from fastapi import HTTPException, status
from utilities.password import Hash_Password
from utilities.data_cleaning import clean_metatdata
import json

def user_registration(data):
    try:
        db = Database()
        hashed_password = Hash_Password.get_password_hash(data.password)
        experience = clean_metatdata(data.experience)
        new_user = {
            "name": data.name,
            "email": data.email,
            "contact": data.contact,
            "dob": data.dob, 
            "company_name": data.company_name,
            "experience": json.dumps(experience) if experience else None,
            "password": hashed_password, 
            "designation": data.designation,
            "role_id": data.role_id  
        }
        result = db.insert_query("users",new_user)
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