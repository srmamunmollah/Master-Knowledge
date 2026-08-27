# Receipt Organisation 2025 - Context

**Owner:** Mamun Mollah (task assigned by Rico; committed to Nikitas)
**Status:** In Progress
**Created:** 2026-08-27
**Deadline:** 2026-09-10 (14 days — Reporting Hub question 1009, Priority A)

## Project Description
Reporting Hub question 1009: verify whether signed 2025 payment receipts exist for
Antonis (Revolut, ~2,000–3,000 EUR/month) and Jennifer (1,750 EUR cash/month), collect
whatever is missing, and set up a standard form + filing location going forward.

## Current Status
- [x] Checked for existing 2025 signed receipts — **none found** for either person, any month.
- [x] Built month-by-month tracker (all 24 records currently MISSING).
- [x] Designed the standard "Signed Payment Receipt" form to use going forward.
- [x] Generated 24 DRAFT (unsigned) pre-filled receipts — one per month per person —
      ready to be signed. **These are NOT valid proof of payment until actually signed**
      and the amount is confirmed against the real payment record.
- [ ] Send drafts to Antonis / Jennifer (or whoever collects signatures) and get them
      actually signed.
- [ ] Replace each DRAFT PDF with the real signed scan as it comes back.
- [ ] Post the answer to Reporting Hub question 1009 (draft prepared, see Files).
- [ ] Message sent to Nikitas asking if he already holds any signed copies (awaiting reply).

## Details
- **Company:** Skynet Holdings Ltd (confirm exact legal entity name before finalizing forms)
- **Antonis:** Revolut transfer, amount varies ~2,000–3,000 EUR/month — confirm exact
  figures against the Revolut export before finalizing each receipt.
- **Jennifer:** Cash, stated as 1,750 EUR/month — confirm against petty cash / cash log
  before finalizing each receipt.
- **Why receipts matter:** cash and Revolut payments to individuals need a signed
  acknowledgment as an audit trail; none existed for 2025 before this task.

## Files
- `2025_Receipt_Tracker_Antonis_Jennifer.xlsx` — living tracker, update status per
  month as signed receipts are actually collected (MISSING → COLLECTED).
- `Signed_Payment_Receipt_Template.docx` — blank template to use for all future
  monthly payments to Antonis and Jennifer (and similar recurring cash/Revolut payments).
- `Answer_to_Question_1009.md` — draft answer/comment for the Reporting Hub ticket.
- `Receipts/Antonis/2025-01..12_Antonis_Receipt_DRAFT.pdf` — 12 draft receipts,
  unsigned, amount left blank.
- `Receipts/Jennifer/2025-01..12_Jennifer_Receipt_DRAFT.pdf` — 12 draft receipts,
  unsigned, amount left blank.

### Receipt Naming Convention
`YYYY-MM_[Name]_Receipt_DRAFT.pdf` while unsigned; drop `_DRAFT` once the real
signed PDF replaces it (`2025-01_Antonis_Receipt.pdf`).

## Technical Notes
- Draft receipts generated with docx (Node) + LibreOffice PDF export, one doc per
  month/person, amount field intentionally left blank per Mamun's instruction —
  amounts must come from real payment records, not be invented.
- Each draft is clearly stamped "DRAFT — PENDING SIGNATURE" so it can never be
  mistaken for genuine proof of payment if filed before being signed.

## Next Steps
1. Confirm real monthly amounts (Revolut export for Antonis, cash log for Jennifer).
2. Send drafts out for actual signature; file signed PDFs over the drafts.
3. Update tracker as each one comes back; report any month still missing at the
   14-day deadline with a specific reason and revised date.
4. Post the Reporting Hub 1009 answer once at least the first batch of signed
   receipts (or a confirmed remediation status) is ready.

## Notes
- Nikitas may already hold signed copies — Mamun messaged him to check before this
  collection effort duplicates anything.
