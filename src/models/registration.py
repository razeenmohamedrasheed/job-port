from pydantic import BaseModel
from typing import Optional, Dict, Any

class Recruiter(BaseModel):
    name:str
    email:str
    contact:str
    dob:str
    company_name:str
    experience:int
    password:str
    designation:str

class Candidate(BaseModel):
    name:str
    email:str
    contact:str
    dob:str
    company_name:Optional[str]
    experience: Optional[Dict[str, Any]] = None
    password:str
    designation:str
