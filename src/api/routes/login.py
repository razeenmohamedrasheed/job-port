from fastapi import APIRouter
from models.registration import Login
from api.handler import login

router = APIRouter(prefix="/auth", tags=["login"])

@router.post('/login')
def recruiter_registeration(payload:Login):
    return login.user_login(payload)