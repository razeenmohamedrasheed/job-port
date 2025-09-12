from fastapi import APIRouter
from models.registration import Recruiter
from api.handler import registration

router = APIRouter()

@router.post('/recruiter')
def registeration(payload:Recruiter):
    return registration.register_recruiter(payload)