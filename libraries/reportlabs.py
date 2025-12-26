from reportlab.pdfgen import canvas
from datetime import datetime

# Create a new PDF file
c = canvas.Canvas("simple_bill.pdf")

# Set title and font
c.setFont("Helvetica-Bold", 18)
c.drawString(150, 800, "Blue Moon Hotel")

c.setFont("Helvetica", 12)
c.drawString(50, 770, "----- Simple Bill Receipt -----")

# Sample data (later you’ll read this from C++ file)
guest_name = "Rohit Mehta"
room_no = "101"
room_type = "Single"
price = 1500
days = 2
total = price * days
payment_mode = "Cash"

# Write data to PDF
c.drawString(50, 740, f"Guest Name: {guest_name}")
c.drawString(50, 720, f"Room Number: {room_no}")
c.drawString(50, 700, f"Room Type: {room_type}")
c.drawString(50, 680, f"Price per Night: Rs.{price}")
c.drawString(50, 660, f"Days Stayed: {days}")
c.drawString(50, 640, f"Total Amount: Rs.{total}")
c.drawString(50, 620, f"Payment Mode: {payment_mode}")
c.drawString(50, 600, f"Date: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
c.drawString(50, 570, "Thank you for staying with us!")

# Save the PDF
c.save()

print("✅ Bill generated successfully: simple_bill.pdf")
