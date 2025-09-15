from pydantic import BaseModel
from typing import Optional, Dict, Any

class Registration(BaseModel):
    name:str
    email:str
    contact:str
    dob:str
    company_name:Optional[str]
    experience: Optional[Dict[str, Any]] = None
    password:str
    designation:str
    role_id:int
class Login(BaseModel):
    email:str
    mobile_nu:Optional[str]
    password:str