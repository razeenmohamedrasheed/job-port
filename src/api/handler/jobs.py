from fastapi import HTTPException, status
from db.database import Database

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
