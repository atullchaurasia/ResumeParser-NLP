# Resume Parser

A Resume Parser built using FastAPI and NLP techniques to extract useful information from resumes in different formats such as PDF and DOCX. The project utilizes various Python libraries for text extraction and processing to parse information like education, experience, skills, projects, certifications, awards, and more.

## Features

- **File Upload API**: Accepts resume files in PDF and DOCX formats.
- **Text Extraction**: Extracts text from resumes using `pdf2image`, `pytesseract`, and `docx2txt`.
- **Information Parsing**: Uses NLP techniques to parse and extract specific sections such as Education, Experience, Skills, Projects, Certifications, Awards, and more.
- **Named Entity Recognition**: Extracts named entities such as email, phone number, and links using regex and NLP.
- **Part-of-Speech (POS) Tagging**: Provides POS tagging of the extracted text using NLTK.
- **Word Frequency Analysis**: Analyzes and provides the frequency distribution of the most common words in the resume.

## Technologies Used

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python.
- **uvicorn**: ASGI server for running the FastAPI app.
- **pdf2image**: Converts PDF to images.
- **pytesseract**: Optical Character Recognition (OCR) for extracting text from images.
- **docx2txt**: Extracts text from DOCX files.
- **NLTK**: Natural Language Toolkit for NLP tasks such as tokenization, POS tagging, and frequency distribution.
- **spaCy**: NLP library for text processing and extracting named entities.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/resume-parser.git
    cd resume-parser
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Install Tesseract OCR:

   - **Windows**: [Download and Install Tesseract OCR](https://github.com/tesseract-ocr/tesseract/wiki)
   - **Linux**: Install via package manager (`sudo apt-get install tesseract-ocr`)
   - **MacOS**: Install via Homebrew (`brew install tesseract`)

5. Configure the path to Tesseract executable in the code (FileService class).

## Running the Application

1. Run the FastAPI server:

    ```bash
    uvicorn main:app --reload
    ```

2. Open your browser and go to `http://127.0.0.1:8000/docs` to access the interactive API documentation provided by FastAPI.

## API Endpoints

- **POST /uploadfile**: Upload a resume file in PDF or DOCX format.
  - **Request**: `file` (required) - File to be uploaded (PDF or DOCX).
  - **Response**: JSON object containing extracted information such as `name`, `email_id`, `mobile_number`, `education`, `experience`, `skills`, `projects`, `certifications`, `awardsection`, `about`, `links`, `other`, `pos_tags`, and `words_freq`.

## Project Structure

```bash
resume-parser/
│
├── app/
│   ├── routers/
│   │   └── file_router.py   # API Router for handling file upload
│   ├── controllers/
│   │   └── file_controller.py   # Controller logic for processing files
│   ├── services/
│   │   └── file_service.py   # Services for handling file operations and text extraction
│   ├── models/
│   │   └── llama_model.py   # Model integration (currently commented out)
│   └── utils/
│       └── file_utils.py   # Utilities for NLP processing
│
├── main.py   # Entry point of the FastAPI application
└── requirements.txt   # Python dependencies
```

## Future Enhancements

- Integration with a machine learning model (e.g., LLaMA or GPT) for better contextual understanding and classification.
- Support for more file formats (e.g., HTML, TXT).
- Enhance the text extraction and parsing logic for more robust and accurate results.
- Add more endpoints to provide additional functionalities like bulk resume parsing, and matching resumes to job descriptions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) for details on the code of conduct and the process for submitting pull requests.

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [pdf2image](https://pypi.org/project/pdf2image/)
- [pytesseract](https://github.com/madmaze/pytesseract)
- [docx2txt](https://pypi.org/project/docx2txt/)
- [NLTK](https://www.nltk.org/)
- [spaCy](https://spacy.io/)

---
