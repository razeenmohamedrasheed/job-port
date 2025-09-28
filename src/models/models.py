from pydantic import BaseModel

class NewJob(BaseModel):
    job_name:str
    description:str
    experience:int
    skills: list
    created_by:int