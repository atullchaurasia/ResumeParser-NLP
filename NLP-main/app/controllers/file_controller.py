from fastapi import UploadFile
from app.services.file_service import FileService
from app.models.llama_model import LlamaModel
from app.utils.file_utils import *
import os

class FileController:
    @staticmethod
    async def handle_file_upload(file: UploadFile):
        try:
            os.makedirs("files", exist_ok=True)
            file_location = f"files/{file.filename}"
            FileService.save_uploaded_file(file, file_location)
            
            if file.filename.endswith('.pdf'):
                output_folder = "images"
                image_files = FileService.pdf_to_jpg(file_location, output_folder)
                if not image_files:
                    return {"error": "Unable to process the PDF file"}
                text = FileService.extract_text_from_images(image_files)
            elif file.filename.endswith('.docx'):
                text = FileService.extract_text_from_docx(file_location)
            else:
                return {"error": "Unsupported file format"}

            stop_headers_list = [
                "EDUCATION", "EDUCATION QUALIFICATION", "EDUCATIONAL QUALIFICATIONS", "WORK HISTORY", "WORK EXPERIENCE", "MAJOR PROJECTS",
                "MINOR PROJECTS", "PROJECTS", "TRAININGS AND WORKSHOPS", "EXTRA-CURRICULAR ACTIVITIES", "QUALIFICATION", 
                "ADDITIONAL SKILLS", "TECHNICAL SKILLS", "CERTIFICATIONS", "ACADEMIC QUALIFICATIONS", "KEY STRENGTHS", "SUMMARY", "AWARDS", 
                "AWARDS AND RECOGNITIONS", "ABOUT","ABOUT ME", "PROJECTS", "SKILLS", "PERSONAL INFORMATION", 
            ]

            education_section = clean_text(extract_section(text, ["EDUCATION", "QUALIFICATION", "EDUCATIONAL QUALIFICATIONS", "ACADEMIC QUALIFICATIONS"], stop_headers_list))
            experience_section = clean_text(extract_section(text, ["WORK EXPERIENCE", "WORK HISTORY", "PROFESSIONAL EXPERIENCE", "EXPERIENCE"], stop_headers_list))
            project_section = clean_text(extract_section(text, ["PROJECTS", "MAJOR PROJECTS", "MINI PROJECTS", "PROJECT DETAILS", "PROJECT DETAILS:"], stop_headers_list))
            skills_section = clean_text(extract_section(text, ["ADDITIONAL SKILLS", "SKILLS", "TECHNICAL SKILLS", "TECHNICAL EXPERTISE", "TECHNICAL EXPERTISE:", "TECHNOLOGY", "PROGRAMMING SKILLS", "TECHNICAL PROFILE", "LANGUAGES AND FRAMEWORKS", "TOOLS & PLATFORMS", "TOOLS", "FRAMEWORKS"], stop_headers_list))
            award_section = clean_text(extract_section(text, ["AWARDS", "AWARDS AND RECOGNITONS"], stop_headers_list))
            about_section = clean_text(extract_section(text, ["ABOUT", "ABOUT ME"], stop_headers_list))
            certificate_section = clean_text(extract_section(text, ["CERTIFICATION", "CERTIFICATIONS"], stop_headers_list))
            email_id = extract_email_id(text)
            mobile_number = extract_mobile_number(text)
            candidate_name = extract_candidate_name(text)
            links = extract_links_extended(text)
            other = find_unmatched_text(text, email_id, candidate_name, mobile_number, education_section, experience_section, skills_section, project_section, award_section, about_section, " ".join(links))
            pos_tags = pos_words_tokenize(text)
            words_frequency = word_frequency_distribution(text)

            #llama_model = LlamaModel()
            #query_input = (
             #   f'{education_section} '
             #   f'{experience_section} '
            #    f'{skills_section} '
             #   f'{project_section} '
             #   f'{certificate_section} '      
             #   f'{award_section} '
             #   f'{about_section} '
             #   f'{" ".join(links)} '
             #   f'{other}'
           # )

          #  response = llama_model.query_llama(query_input)

            return {
                "name": candidate_name,
                "email_id": email_id,
                "mobile_number": mobile_number,
                "education": education_section,
                "experience": experience_section,
                "skills": skills_section,
                "projects": project_section,
                "certifications": certificate_section,
                "awardsection": award_section,
                "about": about_section,
                "links": links,
                "other": other,
                "pos_tags": pos_tags,
                "words_freq":words_frequency,
              #  "response": response,
            }
        except Exception as e:
            return {"error": str(e)}
