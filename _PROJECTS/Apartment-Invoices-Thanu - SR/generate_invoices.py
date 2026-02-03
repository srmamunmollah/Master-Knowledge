#!/usr/bin/env python3
"""
Invoice Generator for Krish Lee Holiday Services
Generates beautiful PDF invoices from Excel data using ReportLab
"""

import pandas as pd
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm, inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_CENTER, TA_RIGHT, TA_LEFT
from datetime import datetime
import os

# Configuration
COMPANY_NAME = "KRISH LEE HOLIDAY SERVICES CY"
COMPANY_ADDRESS_LINE1 = "Lefkonos, 7A"
COMPANY_ADDRESS_LINE2 = "6013, Larnaca"
COMPANY_ADDRESS_LINE3 = "Cyprus"
COMPANY_REG = "HE410185"
TAX_RATE = 0.09
CURRENT_DATE = datetime.now().strftime("%d/%m/%y")

# Colors
PRIMARY_COLOR = colors.HexColor('#1a5f7a')
LIGHT_BLUE = colors.HexColor('#e8f4f8')
HEADER_BG = colors.HexColor('#4a9bb8')


def generate_invoice_pdf(invoice_num, guest_name, property_name, nights, price, output_path):
    """Generate a PDF invoice using ReportLab"""

    # Calculate tax (price includes tax)
    net_amount = price / (1 + TAX_RATE)
    tax_amount = price - net_amount

    # Create the PDF
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4

    # Margins and positioning
    left_margin = 20 * mm
    right_margin = width - 20 * mm

    # Start content much lower to avoid any clipping
    header_y = height - 45 * mm

    # ============ HEADER SECTION ============

    # Row 1: Company Name on left
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(PRIMARY_COLOR)
    c.drawString(left_margin, header_y, COMPANY_NAME)

    # INVOICE title - positioned slightly lower to avoid clipping
    c.setFont("Helvetica-Bold", 20)
    c.drawRightString(right_margin, header_y - 5, "INVOICE")

    # Row 2+: Company Address on left
    c.setFont("Helvetica", 10)
    c.setFillColor(colors.HexColor('#555555'))
    y = header_y - 20
    c.drawString(left_margin, y, COMPANY_ADDRESS_LINE1)
    y -= 13
    c.drawString(left_margin, y, COMPANY_ADDRESS_LINE2)
    y -= 13
    c.drawString(left_margin, y, COMPANY_ADDRESS_LINE3)
    y -= 13
    c.drawString(left_margin, y, f"Company Reg. No: {COMPANY_REG}")

    # Invoice details box (right side, starts below INVOICE title)
    box_width = 60 * mm
    box_height = 22 * mm
    box_x = right_margin - box_width
    box_y = header_y - 50

    # Draw box background
    c.setFillColor(LIGHT_BLUE)
    c.roundRect(box_x, box_y, box_width, box_height, 3*mm, fill=1, stroke=0)

    # Draw box border
    c.setStrokeColor(colors.HexColor('#dee2e6'))
    c.setLineWidth(1)
    c.roundRect(box_x, box_y, box_width, box_height, 3*mm, fill=0, stroke=1)

    # Invoice details text
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(colors.HexColor('#555555'))
    c.drawString(box_x + 5*mm, box_y + box_height - 10*mm, "DATE:")
    c.drawString(box_x + 5*mm, box_y + box_height - 20*mm, "INVOICE #:")

    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(PRIMARY_COLOR)
    c.drawRightString(box_x + box_width - 5*mm, box_y + box_height - 10*mm, CURRENT_DATE)
    c.drawRightString(box_x + box_width - 5*mm, box_y + box_height - 20*mm, str(invoice_num))

    # ============ BILL TO SECTION ============

    bill_to_y = header_y - 90

    # Bill To box
    bill_box_width = 80 * mm
    bill_box_height = 25 * mm

    # Left accent bar
    c.setFillColor(PRIMARY_COLOR)
    c.rect(left_margin, bill_to_y - bill_box_height, 3*mm, bill_box_height, fill=1, stroke=0)

    # Box background
    c.setFillColor(LIGHT_BLUE)
    c.rect(left_margin + 3*mm, bill_to_y - bill_box_height, bill_box_width - 3*mm, bill_box_height, fill=1, stroke=0)

    # Bill To label
    c.setFont("Helvetica", 8)
    c.setFillColor(colors.HexColor('#888888'))
    c.drawString(left_margin + 8*mm, bill_to_y - 8*mm, "BILL TO:")

    # Guest name
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(colors.HexColor('#333333'))
    c.drawString(left_margin + 8*mm, bill_to_y - 18*mm, guest_name[:35])  # Truncate if too long

    # Customer ID (right side)
    c.setFont("Helvetica", 8)
    c.setFillColor(colors.HexColor('#888888'))
    c.drawRightString(right_margin, bill_to_y - 5*mm, "Customer ID")

    c.setFont("Helvetica-Bold", 16)
    c.setFillColor(PRIMARY_COLOR)
    c.drawRightString(right_margin, bill_to_y - 18*mm, str(invoice_num))

    # ============ ITEMS TABLE ============

    table_top = bill_to_y - 50 * mm
    table_width = right_margin - left_margin

    # Table header
    c.setFillColor(PRIMARY_COLOR)
    c.rect(left_margin, table_top - 10*mm, table_width, 10*mm, fill=1, stroke=0)

    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(colors.white)
    c.drawString(left_margin + 5*mm, table_top - 7*mm, "DESCRIPTION")
    c.drawRightString(right_margin - 5*mm, table_top - 7*mm, "AMOUNT")

    # Table row
    row_y = table_top - 10*mm
    row_height = 15 * mm

    # Row background (alternating)
    c.setFillColor(colors.white)
    c.rect(left_margin, row_y - row_height, table_width, row_height, fill=1, stroke=0)

    # Row border
    c.setStrokeColor(colors.HexColor('#eeeeee'))
    c.setLineWidth(0.5)
    c.line(left_margin, row_y - row_height, right_margin, row_y - row_height)

    # Description text
    c.setFont("Helvetica", 11)
    c.setFillColor(colors.HexColor('#333333'))
    description = f"{property_name} For {int(nights)} Night(s)"
    # Truncate if too long
    if len(description) > 55:
        description = description[:52] + "..."
    c.drawString(left_margin + 5*mm, row_y - 10*mm, description)

    # Amount
    c.setFont("Helvetica-Bold", 11)
    c.drawRightString(right_margin - 5*mm, row_y - 10*mm, f"€ {price:.2f}")

    # Empty rows for visual balance
    for i in range(3):
        row_y -= row_height
        c.setStrokeColor(colors.HexColor('#eeeeee'))
        c.line(left_margin, row_y, right_margin, row_y)

    # ============ TOTALS SECTION ============

    totals_y = row_y - 20 * mm
    totals_width = 65 * mm
    totals_x = right_margin - totals_width

    # Totals rows
    row_h = 8 * mm

    # TOTAL row (header)
    c.setFillColor(LIGHT_BLUE)
    c.rect(totals_x, totals_y, totals_width, row_h, fill=1, stroke=0)
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(colors.HexColor('#333333'))
    c.drawString(totals_x + 3*mm, totals_y + 2*mm, "TOTAL")
    c.drawRightString(totals_x + totals_width - 3*mm, totals_y + 2*mm, f"€ {price:.2f}")

    # TAX RATE row
    totals_y -= row_h
    c.setStrokeColor(colors.HexColor('#eeeeee'))
    c.line(totals_x, totals_y, totals_x + totals_width, totals_y)
    c.setFont("Helvetica", 10)
    c.setFillColor(colors.HexColor('#333333'))
    c.drawString(totals_x + 3*mm, totals_y + 2*mm, "TAX RATE")
    c.drawRightString(totals_x + totals_width - 3*mm, totals_y + 2*mm, "9.00%")

    # TAX (incl.) row
    totals_y -= row_h
    c.line(totals_x, totals_y, totals_x + totals_width, totals_y)
    c.drawString(totals_x + 3*mm, totals_y + 2*mm, "TAX (incl.)")
    c.drawRightString(totals_x + totals_width - 3*mm, totals_y + 2*mm, f"-€ {tax_amount:.2f}")

    # OTHER row
    totals_y -= row_h
    c.line(totals_x, totals_y, totals_x + totals_width, totals_y)
    c.drawString(totals_x + 3*mm, totals_y + 2*mm, "OTHER")
    c.drawRightString(totals_x + totals_width - 3*mm, totals_y + 2*mm, "€ -")

    # FINAL TOTAL row
    totals_y -= row_h
    c.setFillColor(PRIMARY_COLOR)
    c.rect(totals_x, totals_y, totals_width, row_h, fill=1, stroke=0)
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(colors.white)
    c.drawString(totals_x + 3*mm, totals_y + 2*mm, "TOTAL")
    c.drawRightString(totals_x + totals_width - 3*mm, totals_y + 2*mm, f"€ {price:.2f}")

    # ============ COMMENTS SECTION ============

    comments_y = totals_y + 4 * row_h
    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(PRIMARY_COLOR)
    c.drawString(left_margin, comments_y, "OTHER COMMENTS")

    c.setFont("Helvetica", 9)
    c.setFillColor(colors.HexColor('#555555'))
    comments_y -= 12
    c.drawString(left_margin, comments_y, "1. Total payment due in 15 days")
    comments_y -= 12
    c.drawString(left_margin, comments_y, "2. Please include the invoice number on your transfer")
    comments_y -= 12
    c.drawString(left_margin, comments_y, "3. Payment Method")

    # Payment method checkboxes
    comments_y -= 15
    checkbox_size = 4 * mm

    # Cash
    c.setStrokeColor(PRIMARY_COLOR)
    c.setLineWidth(1.5)
    c.rect(left_margin + 5*mm, comments_y, checkbox_size, checkbox_size, fill=0, stroke=1)
    c.setFont("Helvetica", 9)
    c.setFillColor(colors.HexColor('#555555'))
    c.drawString(left_margin + 12*mm, comments_y + 1*mm, "Cash")

    # Bank Transfer
    c.rect(left_margin + 35*mm, comments_y, checkbox_size, checkbox_size, fill=0, stroke=1)
    c.drawString(left_margin + 42*mm, comments_y + 1*mm, "Bank Transfer")

    # Cheque
    c.rect(left_margin + 75*mm, comments_y, checkbox_size, checkbox_size, fill=0, stroke=1)
    c.drawString(left_margin + 82*mm, comments_y + 1*mm, "Cheque")

    # ============ SIGNATURES SECTION ============

    sig_y = totals_y - 30 * mm

    c.setFont("Helvetica", 10)
    c.setFillColor(colors.HexColor('#555555'))
    c.drawString(left_margin, sig_y + 15*mm, "Issued by:")
    c.drawString(right_margin - 60*mm, sig_y + 15*mm, "Received by:")

    # Signature lines
    c.setStrokeColor(colors.HexColor('#333333'))
    c.setLineWidth(1)
    c.line(left_margin, sig_y, left_margin + 70*mm, sig_y)
    c.line(right_margin - 70*mm, sig_y, right_margin, sig_y)

    # ============ FOOTER ============

    footer_y = 25 * mm

    # Decorative line
    c.setStrokeColor(PRIMARY_COLOR)
    c.setLineWidth(2)
    c.line(left_margin, footer_y + 15*mm, right_margin, footer_y + 15*mm)

    # Thank you message
    c.setFont("Helvetica-BoldOblique", 14)
    c.setFillColor(PRIMARY_COLOR)
    c.drawCentredString(width / 2, footer_y, "Thank You For Your Business!")

    # Save the PDF
    c.save()

    return output_path


def main(sample_only=False, sample_count=3):
    """Main function to generate invoices"""

    # Read Excel file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    excel_path = os.path.join(script_dir, "January Accounting Report.xlsx")

    df = pd.read_excel(excel_path, header=2)

    # Rename columns for easier access
    df.columns = ['InvoiceNum', 'Status', 'FullName', 'Property', 'Room', 'Nights', 'FirstNight', 'CheckOut', 'Price', 'Referrer']

    # Filter out the TOTAL row and any invalid rows
    df = df[df['Status'] == 'Confirmed']
    df = df.dropna(subset=['InvoiceNum', 'FullName', 'Price'])

    # Create output directory
    output_dir = os.path.join(script_dir, "Invoices")
    os.makedirs(output_dir, exist_ok=True)

    # Limit to sample if requested
    if sample_only:
        df = df.head(sample_count)

    # Generate invoices
    generated = []
    for idx, row in df.iterrows():
        invoice_num = int(row['InvoiceNum'])
        guest_name = str(row['FullName'])
        property_name = str(row['Property'])
        nights = row['Nights']
        price = float(row['Price'])

        output_path = os.path.join(output_dir, f"Invoice_{invoice_num}.pdf")

        try:
            generate_invoice_pdf(invoice_num, guest_name, property_name, nights, price, output_path)
            generated.append(output_path)
            print(f"Generated: Invoice_{invoice_num}.pdf")
        except Exception as e:
            print(f"Error generating invoice {invoice_num}: {e}")

    print(f"\nTotal invoices generated: {len(generated)}")
    print(f"Output directory: {output_dir}")

    return generated


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "--sample":
        main(sample_only=True, sample_count=3)
    else:
        main()
