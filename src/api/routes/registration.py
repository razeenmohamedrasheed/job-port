from fastapi import APIRouter
from models.registration import Recruiter, Candidate
from api.handler import registration

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post('/recruiter')
def recruiter_registeration(payload: Recruiter):
    return registration.register_recruiter(payload)

@router.post('/candidate')
def candidate_registeration(payload: Candidate):
    return registration.register_candidate(payload)
