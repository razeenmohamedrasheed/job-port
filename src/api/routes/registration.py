from fastapi import APIRouter
from models.registration import Registration
from api.handler import registration

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post('/register')
def recruiter_registeration(payload: Registration):
    return registration.user_registration(payload)

