# Changelog

Chronological documentation of all changes.

---

### 2026-08-27
- **Mamun Mollah** - Receipt Organisation 2025 (Reporting Hub Q1009) started
  - Task assigned by Rico; Rico had already committed an answer to Nikitas
  - Checked for 2025 signed payment receipts from Antonis (Revolut) and Jennifer (cash) — none exist for any month
  - Built month-by-month tracker, all 24 records marked MISSING: `Receipt-Organisation-2025 - SR/2025_Receipt_Tracker_Antonis_Jennifer.xlsx`
  - Designed standard signed-receipt form: `Receipt-Organisation-2025 - SR/Signed_Payment_Receipt_Template.docx`
  - Generated 24 DRAFT (unsigned, amount left blank) receipts for retroactive collection: `Receipt-Organisation-2025 - SR/Receipts/Antonis/` and `.../Jennifer/`
  - Drafted answer for Reporting Hub 1009: `Receipt-Organisation-2025 - SR/Answer_to_Question_1009.md`
  - Messaged Nikitas to check whether he already holds any signed copies before duplicating collection effort
  - New project added to `projects-index.md`
  - Next: confirm real monthly amounts, get drafts actually signed, replace DRAFT PDFs with signed scans, post Reporting Hub answer

### 2026-07-17
- **Steve Rogers** - Telegram Boss Tasks app built
  - New self-contained project: Node.js/Express + better-sqlite3 + plain HTML/JS frontend
  - Turns boss's Telegram group messages into a trackable task list (To Do / In Progress / Done)
  - Long-polls Telegram `getUpdates` (LAN-only, no tunneling/webhooks); filters to one group + one sender, dedups by `update_id`
  - Two hardcoded roles: owner (full control) and viewer (read-only) via session auth
  - Verified: npm install/start clean, seed script for placeholder tasks, status updates persist across restart, role-based access control enforced (401/403 checked via curl + browser)
  - Not yet connected to a real bot — Steve still needs to create it via @BotFather and fill in `.env`
  - Output: `_PROJECTS/Telegram-Boss-Tasks - SR/`

### 2026-07-17 (deployment)
- **Steve Rogers** - Telegram Boss Tasks deployed to the Hetzner server
  - Reason: original laptop/same-WiFi design broke once Steve (Bangladesh) and his boss (Cyprus) needed access from different countries
  - Installed Node 20 + certbot on 95.217.207.92; app now runs under systemd (`telegram-boss-tasks.service`) as a dedicated unprivileged user `tgtasks`
  - nginx reverse proxy + free Let's Encrypt HTTPS cert for `95-217-207-92.sslip.io` (no domain purchase needed)
  - App port bound to `127.0.0.1` only; confirmed not reachable directly from the internet
  - Verified login, health check, and task list all work over the public HTTPS URL
  - Still needs real `BOT_TOKEN`/`GROUP_CHAT_ID`/`BOSS_USER_ID` from Steve to go fully live
  - Output: `_PROJECTS/Telegram-Boss-Tasks - SR/CONTEXT.md`

### 2026-06-08
- **Steve Rogers** - Apartment Invoices for Thanu - May 2026 completed
  - Adapted generate_invoices.py for May data (generate_invoices_may.py)
  - Generated 381 professional PDF invoices from Excel data
  - Invoices for Krish Lee Holiday Services CY (May bookings)
  - Invoice range: #20775 - #21155, Total: €34,635.94
  - Invoice date: 31/05/26
  - Output: `_PROJECTS/Apartment-Invoices-Thanu - May/Invoices/`

### 2026-06-06
- **Steve Rogers** - Apartment Invoices for Thanu - April 2026 completed
  - Adapted generate_invoices.py for April data
  - Generated 352 professional PDF invoices from Excel data
  - Invoices for Krish Lee Holiday Services CY (April bookings)
  - Invoice range: #20423 - #20774, Total: €29,063.07
  - Invoice date: 30/04/26
  - Output: `_PROJECTS/Apartment-Invoices-Thanu - Apr/Invoices/`

### 2026-03-04
- **Steve Rogers** - Apartment Invoices for Thanu - February 2026 completed
  - Adapted generate_invoices.py for February data
  - Generated 275 professional PDF invoices from Excel data
  - Invoices for Krish Lee Holiday Services CY (February bookings)
  - Invoice range: #19782 - #20056, Total: €20,762.90
  - Output: `_PROJECTS/Apartment-Invoices-Thanu - Feb/Invoices/`

- **Steve Rogers** - Apartment Invoices for Muthu - February 2026 completed
  - Adapted generate_invoices.py for February data
  - Generated 31 professional PDF invoices from Excel data
  - Invoices for Muthu Cleaning and Maintenance Services Ltd (February bookings)
  - Invoice range: #967 - #997, Total: €2,149.36
  - Output: `_PROJECTS/Apartment-Invoices-Muthu - Feb/Invoices/`

- **Steve Rogers** - MIM (Mimi's Sunny Beach Apartment) Invoices - February 2026 completed
  - Built custom invoice template from reference PDF (230.pdf)
  - Extracted logo, added Unicode font support (Polish/Cyrillic/Czech)
  - Includes booking info with reference numbers, check-in/out dates
  - Generated 8 professional PDF invoices (Epifania CY)
  - Invoice range: #230 - #237, Total: €1,510.73
  - Output: `_PROJECTS/MIM/Invoices/`

### 2026-02-04
- **Steve Rogers** - Apartment Invoices for Muthu completed
  - Created invoice generator script (generate_invoices.py)
  - Used ReportLab for PDF generation
  - Generated 37 professional PDF invoices from Excel data
  - Invoices for Muthu Cleaning and Maintenance Services Ltd (January bookings)
  - Invoice date: 31/01/26
  - Output: `_PROJECTS/Apartment-Invoices-Muthu - SR/Invoices/`

### 2026-02-03
- **Steve Rogers** - Apartment Invoices Project completed
  - Created invoice generator script (generate_invoices.py)
  - Used ReportLab for PDF generation
  - Generated 288 professional PDF invoices from Excel data
  - Invoices for Krish Lee Holiday Services CY (January bookings)
  - Output: `_PROJECTS/Apartment-Invoices-Thanu - SR/Invoices/`

### 2025-02-03
- **Steve Rogers** - Initial setup via Team-Onboarding
- Folder structure created (CLAUDE.md, _SYSTEM/, _PROJECTS/)
- 4 test projects created with CONTEXT.md
- Server configured (95.217.207.92)
- Command Center deployed
- GitHub repository initialized and pushed
