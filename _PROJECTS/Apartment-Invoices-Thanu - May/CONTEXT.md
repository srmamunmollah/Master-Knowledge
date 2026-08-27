# Apartment Invoices for Thanu - May 2026

**Owner:** Steve Rogers (SR)
**Status:** Completed
**Created:** 2026-06-08
**Completed:** 2026-06-08

## Project Description
Automated invoice generation for Krish Lee Holiday Services CY — May 2026 bookings. Same system as January/February/April, adapted for the new month's data.

## Current Status
- [x] Received May Accounting Report.xlsx
- [x] Adapted generate_invoices.py for May data (generate_invoices_may.py)
- [x] Generated all 381 invoices successfully

## Details
- **Company:** Krish Lee Holiday Services CY (Reg. HE410185)
- **Location:** Lefkonos 7A, 6013 Larnaca, Cyprus
- **Tax Rate:** 9% (included in price)
- **Data Source:** May Accounting Report.xlsx (382 rows, 381 confirmed bookings)
- **Invoice Range:** #20775 - #21155
- **Total Revenue:** €34,635.94
- **Invoice Date:** 31/05/26
- **Output:** 381 PDF invoices in `/Invoices/` folder

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
- `generate_invoices_may.py` - Main Python script
- `May Accounting Report.xlsx` - Source data
- `Invoices/` - Output folder with 381 PDFs

## Technical Notes
- Same ReportLab-based script as previous months
- Changes from April: Excel filename and invoice date (31/05/26)
- A4 page size, coordinate system: bottom-left origin

## Notes
- Invoice number also used as Customer ID
- Only "Confirmed" status bookings are processed
- TOTAL AMOUNT row in Excel is automatically skipped
- Computed revenue (€34,635.94) matches the spreadsheet's TOTAL AMOUNT row exactly
