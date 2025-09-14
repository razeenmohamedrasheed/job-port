from fastapi import HTTPException, status
from utilities.password import Hash_Password
from db.database import Database


def user_login(data: any):
    # try:
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

        return {
            "status": "success",
            "message": "Login successful",
            "user_id": db_user["id"],
            "email": db_user["email"]
        }

    # except Exception as e:
    #     raise HTTPException(
    #         status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    #         detail=f"Error occurred: {e}"
    #     )
