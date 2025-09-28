from fastapi import HTTPException, status
from db.database import Database
from models.models import NewJob

def list_jobs():
    try:
        db = Database()
        response = db.select_query()
        return {
            "message":"success",
            "response":response
        }
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error occurred: {e}"
        )


def create_jobs(payload:NewJob):
    try:
        db = Database()
        new_user = {
            "job_name":payload.job_name,
            "description":payload.description,
            "experience":payload.experience,
            "skills": payload.skills,
            "created_by":payload.created_by
        }
        result = db.insert_query("jobs",new_user)
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