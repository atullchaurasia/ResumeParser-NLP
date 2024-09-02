import os
import shutil
from pdf2image import convert_from_path
import pytesseract
from PIL import Image
import docx2txt
import re

class FileService:
    @staticmethod
    def pdf_to_jpg(pdf_path, output_folder):
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        try:
            images = convert_from_path(pdf_path, dpi=300)
        except Exception as e:
            return []
        image_files = []
        for i, image in enumerate(images):
            image_file = f'{output_folder}/page_{i + 1}.jpg'
            image.save(image_file, 'JPEG')
            image_files.append(image_file)
        return image_files

    @staticmethod
    def extract_text_from_images(image_files):
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        tessdata_dir_config = '--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"'
        all_text = ""
        for image_file in image_files:
            image = Image.open(image_file)
            text = pytesseract.image_to_string(image, config=tessdata_dir_config)
            all_text += text + "\n"
        return all_text

    @staticmethod
    def extract_text_from_docx(docx_path):
        return docx2txt.process(docx_path)

    @staticmethod
    def save_uploaded_file(file, destination):
        with open(destination, "wb+") as file_object:
            shutil.copyfileobj(file.file, file_object)
