from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_sample_aadhar_pdf(file_path):
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter

    # Draw a rectangle to mimic the Aadhaar card
    c.setFillColorRGB(0.2, 0.5, 0.8)  # Background color
    c.rect(50, height - 250, width - 100, 220, fill=1)

    # Add sample text to the card
    c.setFillColorRGB(1, 1, 1)  # White text
    c.setFont("Helvetica-Bold", 24)
    c.drawString(60, height - 100, "Aadhaar Card")

    c.setFont("Helvetica", 14)
    c.drawString(60, height - 140, "Name: John Doe")
    c.drawString(60, height - 160, "Aadhaar Number: 1234 5678 9012")
    c.drawString(60, height - 180, "Gender: Male")
    c.drawString(60, height - 200, "Date of Birth: 01/01/1990")
    c.drawString(60, height - 220, "Address: 123 Sample Street")
    c.drawString(60, height - 240, "City, State, Country")

    # Draw a border around the card
    c.setStrokeColorRGB(0, 0, 0)  # Border color
    c.rect(50, height - 250, width - 100, 220)

    # Save the PDF
    c.save()

# Create a sample Aadhaar PDF
create_sample_aadhar_pdf("sample_aadhar_card.pdf")
