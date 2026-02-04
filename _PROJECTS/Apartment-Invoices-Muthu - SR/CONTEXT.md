# Apartment Invoices for Muthu - Context

**Owner:** Steve Rogers (SR)
**Status:** Completed
**Created:** 2026-02-04
**Completed:** 2026-02-04

## Project Description
Automated invoice generation system for Muthu Cleaning and Maintenance Services Ltd. Generates professional PDF invoices from Excel booking data for apartment/property rentals in Cyprus.

## Current Status
- [x] Analyzed Excel data structure (January Accounting Report.xlsx)
- [x] Created invoice template matching company design
- [x] Built Python script using ReportLab for PDF generation
- [x] Generated all 37 invoices successfully

## Details
- **Company:** Muthu Cleaning and Maintenance Services Ltd (Reg. HE410185)
- **Location:** Lefkonos 7A, 6013 Larnaca, Cyprus
- **Tax Rate:** 9% (included in price)
- **Data Source:** January Accounting Report.xlsx (37 confirmed bookings)
- **Output:** 37 PDF invoices in `/Invoices/` folder
- **Invoice Date:** 31/01/26 (last day of January 2026)

### Invoice Naming Convention
`Invoice_XXXXX.pdf` where XXXXX is the invoice number from Excel

### Key Features
- Professional layout with company branding
- Automatic tax calculation (backwards from total)
- Fixed date (31/01/26) stamped on each invoice
- Guest name, property, nights, and total amount
- Payment method checkboxes (Cash, Bank Transfer, Cheque)
- Signature lines for Issued by / Received by
- Highlighted "We Appreciate Your Business!" footer

## Files
- `generate_invoices.py` - Main Python script
- `January Accounting Report.xlsx` - Source data
- `Invoices/` - Output folder with 37 PDFs

## Technical Notes
- Uses ReportLab library for PDF generation
- Coordinate system: bottom-left origin
- A4 page size
- Key positioning: header_y = height - 45mm to avoid clipping

## Notes
- Invoice number also used as Customer ID
- Only "Confirmed" status bookings are processed
- TOTAL row in Excel is automatically skipped
