# PDF Aadhar, PAN, GSTIN, CA Number Extractor API

This is a FastAPI-based web service that allows you to upload a PDF (such as an electricity bill) and extract the **CA (Consumer Account) number** using Optical Character Recognition (OCR). The service uses `pdfplumber` and `pytesseract` to extract text from image-based PDF files.

## Features

- Upload a PDF file (image-based or text-based) for the required type of document and extract the its number.
- Supports CA numbers in the format of 12 digits, with or without spaces/dashes.
- Support PAN
- Support GSTIN
- Support Aadhar

## Prerequisites

1. ** Python 3.7+** installed.
2. ** Tesseract OCR** installed on your machine:
   - **Windows**: Download and install [Tesseract-OCR](https://github.com/tesseract-ocr/tesseract/wiki).
   - ** Linux** (Ubuntu):
     ``` bash
     sudo apt install tesseract-ocr
     ```
   - ** macOS** (using Homebrew):
     ``` bash
     brew install tesseract
     ```

## Installation

1. Clone this repository or download the code:
   ``` bash
   git clone https://github.com/singhravi/pdf_data_extractor.git
   cd pdf_data_extractor
   Create a virtual environment:
   ```

2. Create virtual environment
 
`python3 -m venv pdfvenv`
# On MacBook  `source pdfvenv/bin/activate`
# On Windows: `pdfvenv\Scripts\activate`

3. Install the required dependencies:


`pip install -r requirements.txt`

Verify that Tesseract is installed correctly:

`tesseract --version`

4. Usage
Run the FastAPI server using Uvicorn:


`uvicorn main:app --reload`

The --reload option will automatically reload the server when you make code changes.
Open your browser and navigate to the interactive API docs:

(App)[http://127.0.0.1:8000/docs]

Here, you can upload a PDF file (e.g., an electricity bill) to extract the CA number.

API Endpoints
POST /extract-ca-number/

Upload a PDF file to extract the CA number from it. The request should include the file in the form-data format.

Example Request

`curl -X 'POST' \
 'http://127.0.0.1:8000/extract-ca-number/' \
 -H 'accept: application/json' \
 -H 'Content-Type: multipart/form-data' \
 -F 'file=@path_to_your_electricity_bill.pdf'`

Example Response
json

{
"CA Number": "1234 5678 9012"
}

File Structure

pdf_data_extractor/
│
|** templates # folder that contains the jinja2 html files
|** docs # folder containing the sample PDF file
├── main.py # The FastAPI application code
├── requirements.txt # Python dependencies
├── README.md # Documentation
└── pdfvenv/ # Virtual environment directory (not included in the repository)

# Dependencies
- FastAPI: Web framework for building APIs.
- Uvicorn: ASGI server for serving FastAPI applications.
- pdfplumber: Library to extract text from PDFs.
- pytesseract: Python binding for Tesseract OCR.
- Pillow: Python Imaging Library, required for handling images.

Running Tests
You can test the API using Postman, Curl, or the interactive docs (/docs).

License
This project is licensed under the MIT License - see the LICENSE file for details.


### Key Sections of the `README.md`:

- **Project Overview**: Describes the purpose and functionality of the FastAPI app.
- **Prerequisites**: Lists Python and Tesseract OCR as dependencies.
- **Installation**: Provides steps to clone the repository, set up a virtual environment, and install dependencies.
- **Usage**: Describes how to run the FastAPI server and interact with it using the `/extract-ca-number/` endpoint.
- **API Endpoints**: Provides details on the endpoint, including an example request and response.
- **Dependencies**: Lists the main Python packages required by the application.
- **Running Tests**: Mentions how to test the API using Postman, Curl, or the interactive FastAPI docs.

