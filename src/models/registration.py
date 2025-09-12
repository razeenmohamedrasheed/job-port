from pydantic import BaseModel

class Recruiter(BaseModel):
    name:str
    email:str
    contact:str
    dob:str
    company_name:str
    experience:int
    password:str
    designation:str