from fastapi import APIRouter
from api.handler import jobs

router = APIRouter(prefix="/jobs", tags=["jobs"])

@router.get('/all')
def recruiter_registeration():
    return jobs.list_jobs()
