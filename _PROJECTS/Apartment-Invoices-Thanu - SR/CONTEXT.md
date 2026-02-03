# Apartment Invoices for Thanu - Context

**Owner:** Steve Rogers (SR)
**Status:** Completed
**Created:** 2025-02-03
**Completed:** 2026-02-03

## Project Description
Automated invoice generation system for Krish Lee Holiday Services CY. Generates professional PDF invoices from Excel booking data for apartment/property rentals in Cyprus.

## Current Status
- [x] Analyzed Excel data structure (January Accounting Report.xlsx)
- [x] Created invoice template matching company design
- [x] Built Python script using ReportLab for PDF generation
- [x] Generated all 288 invoices successfully

## Details
- **Company:** Krish Lee Holiday Services CY (Reg. HE410185)
- **Location:** Lefkonos 7A, 6013 Larnaca, Cyprus
- **Tax Rate:** 9% (included in price)
- **Data Source:** January Accounting Report.xlsx (289 bookings, 288 confirmed)
- **Output:** 288 PDF invoices in `/Invoices/` folder

### Invoice Naming Convention
`Invoice_XXXXX.pdf` where XXXXX is the invoice number from Excel

### Key Features
- Professional layout with company branding
- Automatic tax calculation (backwards from total)
- Current date stamped on each invoice
- Guest name, property, nights, and total amount
- Payment method checkboxes (Cash, Bank Transfer, Cheque)
- Signature lines for Issued by / Received by

## Files
- `generate_invoices.py` - Main Python script
- `January Accounting Report.xlsx` - Source data
- `Invoice.jpg` - Original design reference
- `Invoices/` - Output folder with 288 PDFs

## Technical Notes
- Uses ReportLab library for PDF generation
- Coordinate system: bottom-left origin
- A4 page size
- Key positioning: header_y = height - 45mm to avoid clipping

## Next Steps
1. Deliver invoices to Thanu
2. Archive project

## Notes
- Invoice number also used as Customer ID
- Only "Confirmed" status bookings are processed
- TOTAL row in Excel is automatically skipped
