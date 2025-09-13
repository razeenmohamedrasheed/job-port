from fastapi import FastAPI
from api.routes import registration
import uvicorn

app = FastAPI()

@app.get("/")
def main_page():
    return {
        "message": "Welcome"
    }

app.include_router(registration.router, prefix="/v1")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
