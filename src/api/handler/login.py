from fastapi import HTTPException, status
from utilities.password import Hash_Password
from utilities.auth import create_access_token,create_refresh_token
from db.database import Database


def user_login(data: any):
    try:
        db = Database()        
        db_user = db.get_user_by_email(data.email)
        if not db_user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid username or password"
            )

        if not Hash_Password.verify_password(data.password, db_user["password"]):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid username or password"
            )
        data = {
            "sub": str(db_user["candidate_id"]),   
            "email": db_user["email"],
            "role": str(db_user["role_id"])
        }
        access_token = create_access_token(data)
        refresh_token = create_refresh_token(data) 
        return{
            "message":"success",
            "access_token":access_token,
            "refresh_token":refresh_token
        }

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error occurred: {e}"
        )
