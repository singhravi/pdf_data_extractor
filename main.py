import pdfplumber
import pytesseract
from PIL import Image
import re

from fastapi import FastAPI, UploadFile, Request, File
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

import io

# Initialize FastAPI app
app = FastAPI()

 #Set the templates directory
templates = Jinja2Templates(directory="templates")

# Set API to open index page
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Function to extract text from image-based Aadhaar PDF using OCR
def extract_text_from_image_based_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            # Extract the image of each page
            pil_image = page.to_image().original  # Get the original PIL image directly
            
            # Use pytesseract to extract text from image
            page_text = pytesseract.image_to_string(pil_image)
            text += page_text + "\n"  # Add newline for separation between pages
    return text

# Function to extract text from image-based PDF using OCR
def extract_text_from_image_based_pdf_bytes(pdf_bytes):
    text = ""
    # Wrap the raw bytes in a BytesIO object to make it file-like
    pdf_file = io.BytesIO(pdf_bytes)
    
    # Open the PDF file using pdfplumber
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            pil_image = page.to_image().original  # Get the original PIL image directly
            # Use pytesseract to extract text from image
            page_text = pytesseract.image_to_string(pil_image)
            text += page_text + "\n"  # Add newline for separation between pages
    return text

# Function to extract Aadhaar card information from extracted text
def extract_aadhaar_info(text):
    data = {}

    # Regex pattern to match Aadhaar number (12 digits with optional spaces)
    aadhaar_pattern = r'\b\d{4}\s\d{4}\s\d{4}\b'
    
    # Aadhaar Number
    aadhaar_number = re.search(aadhaar_pattern, text)
    if aadhaar_number:
        data['Aadhaar Number'] = aadhaar_number.group(0)
    else:
        data['Aadhaar Number'] = 'Not found'

    return data

# Function to extract PAN card information from extracted text
def extract_pan_info(text):
    data = {}

    # Regex pattern to match PAN number (5 letters, 4 digits, 1 letter)
    pan_pattern = r'\b[A-Z]{5}\d{4}[A-Z]\b'
    
    # PAN Number
    pan_number = re.search(pan_pattern, text)
    if pan_number:
        data['PAN Number'] = pan_number.group(0)
    else:
        data['PAN Number'] = 'Not found'

    return data

# Function to extract GSTIN from extracted text
def extract_gstin_info(text):
    data = {}

    # Regex pattern to match GSTIN (15 characters)
    gstin_pattern = r'\b\d{2}[A-Z]{4}\d{4}[A-Z]\d{1}[Z]\d{1}\b'
    
    # GSTIN Number
    gstin_number = re.search(gstin_pattern, text)
    if gstin_number:
        data['GSTIN'] = gstin_number.group(0)
    else:
        data['GSTIN'] = 'Not found'

    return data

# Function to extract CA number from extracted text
def extract_ca_number(text):
    data = {}

    # Regex pattern to match CA number (12 digits, or separated by spaces/dashes)
    ca_pattern = r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}\b'
    
    # CA Number
    ca_number = re.search(ca_pattern, text)
    if ca_number:
        data['CA Number'] = ca_number.group(0)
    else:
        data['CA Number'] = 'Not found'

    return data


# using command line print of information
# Path to the uploaded Aadhaar PDF
aadhar_pdf_path = './docs/sample_aadhar_card.pdf'
# Path to the PAN, CA, GSTIN number PDF file
pan_ca_gstin_pdf_path = './docs/dummy_pan_ca_gstin_card.pdf'

# Extract text from PDF using OCR
aadhar_text = extract_text_from_image_based_pdf(aadhar_pdf_path)

# Extract Aadhaar info from the text
aadhaar_info = extract_aadhaar_info(aadhar_text)

# Output the extracted Aadhaar number
print(aadhaar_info)

# Path to the uploaded Aadhaar PDF
#pan_pdf_path = './docs/pan.pdf'

# Extract text from PDF using OCR
pan_text = extract_text_from_image_based_pdf(pan_ca_gstin_pdf_path)

# Extract PAN info from the text
pan_info = extract_pan_info(pan_text)

# Output the extracted Aadhaar number
print(pan_info)

# Path to the uploaded Aadhaar PDF
# gstin_pdf_path = './docs/gstin.pdf'

# Extract text from PDF using OCR
gstin_text = extract_text_from_image_based_pdf(pan_ca_gstin_pdf_path)

# Extract PAN info from the text
gstin_info = extract_pan_info(gstin_text)

# Output the extracted Aadhaar number
print(gstin_info)


# Path to the uploaded electricity PDF
# electricity_pdf_path = './docs/electricity.pdf'

# Extract CA from PDF using OCR
ca_text = extract_text_from_image_based_pdf(pan_ca_gstin_pdf_path)

# Extract electricity CA info from the text
ca_info = extract_pan_info(ca_text)

# Output the extracted Aadhaar number
print(ca_info)


# using FastAPI
# Define a FastAPI POST route to handle file upload
@app.post("/extract-ca-number/")
async def extract_ca_from_pdf(file: UploadFile = File(...)):
    # Check if the uploaded file is a PDF
    if file.content_type != "application/pdf":
        return JSONResponse(status_code=400, content={"message": "Only PDF files are supported."})
    
    # Read the file bytes
    pdf_bytes = await file.read()
    
    # Extract text from the PDF
    text = extract_text_from_image_based_pdf_bytes(pdf_bytes)
    
    # Extract CA number from the text
    ca_info = extract_ca_number(text)
    
    # Return the extracted CA number as JSON response
    return JSONResponse(content=ca_info)

@app.post("/extract-aadhar-number/")
async def extract_ca_from_pdf(file: UploadFile = File(...)):
    # Check if the uploaded file is a PDF
    if file.content_type != "application/pdf":
        return JSONResponse(status_code=400, content={"message": "Only PDF files are supported."})
    
    # Read the file bytes
    pdf_bytes = await file.read()
    
    # Extract text from the PDF
    text = extract_text_from_image_based_pdf_bytes(pdf_bytes)
    
    # Extract CA number from the text
    aadhar_info = extract_aadhaar_info(text)
    
    # Return the extracted Aadhar number as JSON response
    return JSONResponse(content=aadhar_info)

@app.post("/extract-pan-number/")
async def extract_ca_from_pdf(file: UploadFile = File(...)):
    # Check if the uploaded file is a PDF
    if file.content_type != "application/pdf":
        return JSONResponse(status_code=400, content={"message": "Only PDF files are supported."})
    
    # Read the file bytes
    pdf_bytes = await file.read()
    
    # Extract text from the PDF
    text = extract_text_from_image_based_pdf_bytes(pdf_bytes)
    
    # Extract CA number from the text
    pan_info = extract_pan_info(text)
    
    # Return the extracted Aadhar number as JSON response
    return JSONResponse(content=pan_info)

@app.post("/extract-gstin-number/")
async def extract_ca_from_pdf(file: UploadFile = File(...)):
    # Check if the uploaded file is a PDF
    if file.content_type != "application/pdf":
        return JSONResponse(status_code=400, content={"message": "Only PDF files are supported."})
    
    # Read the file bytes
    pdf_bytes = await file.read()
    
    # Extract text from the PDF
    text = extract_text_from_image_based_pdf_bytes(pdf_bytes)
    
    # Extract CA number from the text
    gstin_info = extract_gstin_info(text)
    
    # Return the extracted Aadhar number as JSON response
    return JSONResponse(content=gstin_info)