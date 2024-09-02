import uvicorn
from fastapi import FastAPI
from app.routers import file_router

app = FastAPI()

app.include_router(file_router.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
