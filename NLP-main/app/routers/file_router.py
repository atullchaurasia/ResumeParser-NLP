from fastapi import APIRouter, UploadFile, File
from app.controllers.file_controller import FileController

router = APIRouter()

@router.post("/uploadfile")
async def upload_file(file: UploadFile = File(...)):
    return await FileController.handle_file_upload(file)

