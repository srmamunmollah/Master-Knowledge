#!/usr/bin/env python3
"""
Invoice Generator for Krish Lee Holiday Services - May 2026
"""

import pandas as pd
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
import os

COMPANY_NAME = "KRISH LEE HOLIDAY SERVICES CY"
COMPANY_ADDRESS_LINE1 = "Lefkonos, 7A"
COMPANY_ADDRESS_LINE2 = "6013, Larnaca"
COMPANY_ADDRESS_LINE3 = "Cyprus"
COMPANY_REG = "HE410185"
TAX_RATE = 0.09
INVOICE_DATE = "31/05/26"  # Last day of May 2026

PRIMARY_COLOR = colors.HexColor('#1a5f7a')
LIGHT_BLUE = colors.HexColor('#e8f4f8')


def generate_invoice_pdf(invoice_num, guest_name, property_name, nights, price, output_path):
    net_amount = price / (1 + TAX_RATE)
    tax_amount = price - net_amount

    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4

    left_margin = 20 * mm
    right_margin = width - 20 * mm
    header_y = height - 45 * mm

    # Header
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(PRIMARY_COLOR)
    c.drawString(left_margin, header_y, COMPANY_NAME)

    c.setFont("Helvetica-Bold", 20)
    c.drawRightString(right_margin, header_y - 5, "INVOICE")

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

    # Invoice details box
    box_width = 60 * mm
    box_height = 22 * mm
    box_x = right_margin - box_width
    box_y = header_y - 50

    c.setFillColor(LIGHT_BLUE)
    c.roundRect(box_x, box_y, box_width, box_height, 3*mm, fill=1, stroke=0)
    c.setStrokeColor(colors.HexColor('#dee2e6'))
    c.setLineWidth(1)
    c.roundRect(box_x, box_y, box_width, box_height, 3*mm, fill=0, stroke=1)

    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(colors.HexColor('#555555'))
    c.drawString(box_x + 5*mm, box_y + box_height - 10*mm, "DATE:")
    c.drawString(box_x + 5*mm, box_y + box_height - 20*mm, "INVOICE #:")

    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(PRIMARY_COLOR)
    c.drawRightString(box_x + box_width - 5*mm, box_y + box_height - 10*mm, INVOICE_DATE)
    c.drawRightString(box_x + box_width - 5*mm, box_y + box_height - 20*mm, str(invoice_num))

    # Bill To
    bill_to_y = header_y - 90
    bill_box_width = 80 * mm
    bill_box_height = 25 * mm

    c.setFillColor(PRIMARY_COLOR)
    c.rect(left_margin, bill_to_y - bill_box_height, 3*mm, bill_box_height, fill=1, stroke=0)

    c.setFillColor(LIGHT_BLUE)
    c.rect(left_margin + 3*mm, bill_to_y - bill_box_height, bill_box_width - 3*mm, bill_box_height, fill=1, stroke=0)

    c.setFont("Helvetica", 8)
    c.setFillColor(colors.HexColor('#888888'))
    c.drawString(left_margin + 8*mm, bill_to_y - 8*mm, "BILL TO:")

    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(colors.HexColor('#333333'))
    c.drawString(left_margin + 8*mm, bill_to_y - 18*mm, guest_name[:35])

    c.setFont("Helvetica", 8)
    c.setFillColor(colors.HexColor('#888888'))
    c.drawRightString(right_margin, bill_to_y - 5*mm, "Customer ID")

    c.setFont("Helvetica-Bold", 16)
    c.setFillColor(PRIMARY_COLOR)
    c.drawRightString(right_margin, bill_to_y - 18*mm, str(invoice_num))

    # Items table
    table_top = bill_to_y - 50 * mm
    table_width = right_margin - left_margin

    c.setFillColor(PRIMARY_COLOR)
    c.rect(left_margin, table_top - 10*mm, table_width, 10*mm, fill=1, stroke=0)

    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(colors.white)
    c.drawString(left_margin + 5*mm, table_top - 7*mm, "DESCRIPTION")
    c.drawRightString(right_margin - 5*mm, table_top - 7*mm, "AMOUNT")

    row_y = table_top - 10*mm
    row_height = 15 * mm

    c.setFillColor(colors.white)
    c.rect(left_margin, row_y - row_height, table_width, row_height, fill=1, stroke=0)

    c.setStrokeColor(colors.HexColor('#eeeeee'))
    c.setLineWidth(0.5)
    c.line(left_margin, row_y - row_height, right_margin, row_y - row_height)

    c.setFont("Helvetica", 11)
    c.setFillColor(colors.HexColor('#333333'))
    description = f"{property_name} For {int(nights)} Night(s)"
    if len(description) > 55:
        description = description[:52] + "..."
    c.drawString(left_margin + 5*mm, row_y - 10*mm, description)

    c.setFont("Helvetica-Bold", 11)
    c.drawRightString(right_margin - 5*mm, row_y - 10*mm, f"€ {price:.2f}")

    for i in range(3):
        row_y -= row_height
        c.setStrokeColor(colors.HexColor('#eeeeee'))
        c.line(left_margin, row_y, right_margin, row_y)

    # Totals
    totals_y = row_y - 20 * mm
    totals_width = 65 * mm
    totals_x = right_margin - totals_width
    row_h = 8 * mm

    c.setFillColor(LIGHT_BLUE)
    c.rect(totals_x, totals_y, totals_width, row_h, fill=1, stroke=0)
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(colors.HexColor('#333333'))
    c.drawString(totals_x + 3*mm, totals_y + 2*mm, "TOTAL")
    c.drawRightString(totals_x + totals_width - 3*mm, totals_y + 2*mm, f"€ {price:.2f}")

    totals_y -= row_h
    c.setStrokeColor(colors.HexColor('#eeeeee'))
    c.line(totals_x, totals_y, totals_x + totals_width, totals_y)
    c.setFont("Helvetica", 10)
    c.setFillColor(colors.HexColor('#333333'))
    c.drawString(totals_x + 3*mm, totals_y + 2*mm, "TAX RATE")
    c.drawRightString(totals_x + totals_width - 3*mm, totals_y + 2*mm, "9.00%")

    totals_y -= row_h
    c.line(totals_x, totals_y, totals_x + totals_width, totals_y)
    c.drawString(totals_x + 3*mm, totals_y + 2*mm, "TAX (incl.)")
    c.drawRightString(totals_x + totals_width - 3*mm, totals_y + 2*mm, f"-€ {tax_amount:.2f}")

    totals_y -= row_h
    c.line(totals_x, totals_y, totals_x + totals_width, totals_y)
    c.drawString(totals_x + 3*mm, totals_y + 2*mm, "OTHER")
    c.drawRightString(totals_x + totals_width - 3*mm, totals_y + 2*mm, "€ -")

    totals_y -= row_h
    c.setFillColor(PRIMARY_COLOR)
    c.rect(totals_x, totals_y, totals_width, row_h, fill=1, stroke=0)
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(colors.white)
    c.drawString(totals_x + 3*mm, totals_y + 2*mm, "TOTAL")
    c.drawRightString(totals_x + totals_width - 3*mm, totals_y + 2*mm, f"€ {price:.2f}")

    # Comments
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

    comments_y -= 15
    checkbox_size = 4 * mm
    c.setStrokeColor(PRIMARY_COLOR)
    c.setLineWidth(1.5)
    c.rect(left_margin + 5*mm, comments_y, checkbox_size, checkbox_size, fill=0, stroke=1)
    c.setFont("Helvetica", 9)
    c.setFillColor(colors.HexColor('#555555'))
    c.drawString(left_margin + 12*mm, comments_y + 1*mm, "Cash")

    c.rect(left_margin + 35*mm, comments_y, checkbox_size, checkbox_size, fill=0, stroke=1)
    c.drawString(left_margin + 42*mm, comments_y + 1*mm, "Bank Transfer")

    c.rect(left_margin + 75*mm, comments_y, checkbox_size, checkbox_size, fill=0, stroke=1)
    c.drawString(left_margin + 82*mm, comments_y + 1*mm, "Cheque")

    # Signatures
    sig_y = totals_y - 30 * mm
    c.setFont("Helvetica", 10)
    c.setFillColor(colors.HexColor('#555555'))
    c.drawString(left_margin, sig_y + 15*mm, "Issued by:")
    c.drawString(right_margin - 60*mm, sig_y + 15*mm, "Received by:")

    c.setStrokeColor(colors.HexColor('#333333'))
    c.setLineWidth(1)
    c.line(left_margin, sig_y, left_margin + 70*mm, sig_y)
    c.line(right_margin - 70*mm, sig_y, right_margin, sig_y)

    # Footer
    footer_y = 25 * mm
    c.setStrokeColor(PRIMARY_COLOR)
    c.setLineWidth(2)
    c.line(left_margin, footer_y + 15*mm, right_margin, footer_y + 15*mm)

    c.setFont("Helvetica-BoldOblique", 14)
    c.setFillColor(PRIMARY_COLOR)
    c.drawCentredString(width / 2, footer_y, "Thank You For Your Business!")

    c.save()
    return output_path


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    excel_path = os.path.join(script_dir, "May Accounting Report.xlsx")

    df = pd.read_excel(excel_path, header=2)
    df.columns = ['InvoiceNum', 'Status', 'FullName', 'Property', 'Room', 'Nights', 'FirstNight', 'CheckOut', 'Price', 'Referrer']

    df = df[df['Status'] == 'Confirmed']
    df = df.dropna(subset=['InvoiceNum', 'FullName', 'Price'])

    output_dir = os.path.join(script_dir, "Invoices")
    os.makedirs(output_dir, exist_ok=True)

    generated = []
    errors = []
    for idx, row in df.iterrows():
        invoice_num = int(row['InvoiceNum'])
        guest_name = str(row['FullName'])
        property_name = str(row['Property'])
        nights = row['Nights']
        price = float(str(row['Price']).strip())

        output_path = os.path.join(output_dir, f"Invoice_{invoice_num}.pdf")

        try:
            generate_invoice_pdf(invoice_num, guest_name, property_name, nights, price, output_path)
            generated.append(output_path)
            print(f"Generated: Invoice_{invoice_num}.pdf")
        except Exception as e:
            print(f"ERROR invoice {invoice_num}: {e}")
            errors.append(invoice_num)

    print(f"\nTotal generated: {len(generated)}")
    if errors:
        print(f"Errors: {errors}")
    print(f"Output: {output_dir}")


if __name__ == "__main__":
    main()
