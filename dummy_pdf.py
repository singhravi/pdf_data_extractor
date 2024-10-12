from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_dummy_pan_ca_gstin_pdf(file_path):
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter

    # Draw a rectangle to mimic the PAN card
    c.setFillColorRGB(0.2, 0.5, 0.8)  # Background color
    c.rect(50, height - 250, width - 100, 200, fill=1)

    # Add sample PAN card details
    c.setFillColorRGB(1, 1, 1)  # White text
    c.setFont("Helvetica-Bold", 24)
    c.drawString(60, height - 150, "PAN Card")

    c.setFont("Helvetica", 14)
    c.drawString(60, height - 170, "Name: John Doe")
    c.drawString(60, height - 190, "PAN Number: ABCDE1234F")

    # Draw a rectangle to mimic the CA number section
    c.setFillColorRGB(0.8, 0.2, 0.2)  # Different background color
    c.rect(50, height - 460, width - 100, 80, fill=1)

    # Add sample CA number details
    c.setFillColorRGB(1, 1, 1)  # White text
    c.setFont("Helvetica-Bold", 20)
    c.drawString(60, height - 410, "CA Number")

    c.setFont("Helvetica", 14)
    c.drawString(60, height - 430, "CA Number: 12345ABC6789")

    # Draw a rectangle to mimic the GSTIN section
    c.setFillColorRGB(0.2, 0.8, 0.2)  # Another background color
    c.rect(50, height - 550, width - 100, 80, fill=1)

    # Add sample GSTIN details
    c.setFillColorRGB(1, 1, 1)  # White text
    c.setFont("Helvetica-Bold", 20)
    c.drawString(60, height - 500, "GSTIN")

    c.setFont("Helvetica", 14)
    c.drawString(60, height - 520, "GSTIN: 12ABCDE3456Z1Z2")

    # Save the PDF
    c.save()

# Create a sample PDF
create_dummy_pan_ca_gstin_pdf("dummy_pan_ca_gstin_card.pdf")
