# MASTER-CONTEXT.md - Steve Rogers's Knowledge Base

Last updated: 2026-07-17

---

## Quick Facts

| Property | Value |
|----------|-------|
| **Name** | Steve Rogers |
| **Abbreviation** | SR |
| **Email** | Sr@skynet-holdings.com |
| **GitHub** | github.com/srmamunmollah |
| **Server** | 95.217.207.92 |
| **Command Center** | http://95.217.207.92:8080 |

---

## Team

| Name | Abbr | Email | Role |
|------|------|-------|------|
| Steve Rogers | SR | Sr@skynet-holdings.com | Owner |

---

## Active Projects

| Project | Status | Priority | Description | Folder |
|---------|--------|----------|-------------|--------|
| Telegram-Boss-Tasks | Deployed, awaiting bot credentials | Medium | Turns boss's Telegram messages into tracked tasks; live at https://95-217-207-92.sslip.io | `_PROJECTS/Telegram-Boss-Tasks - SR/` |
| Website-Redesign | In Progress | High | Test project: Fictional website overhaul | `_PROJECTS/Website-Redesign - SR/` |
| Kunden-Onboarding | In Progress | Medium | Test project: Fictional customer process | `_PROJECTS/Kunden-Onboarding - SR/` |
| Internes-Tool | Ideas | Low | Test project: Fictional internal tool | `_PROJECTS/Internes-Tool - SR/` |
| Mein-Erstes-Projekt | New | - | Empty template for your first real project | `_PROJECTS/Mein-Erstes-Projekt - SR/` |

> **Note:** The first 3 projects are test projects with sample data. You can delete them once you have your own projects.

---

## Folder Structure

```
Master-Knowledge/
├── CLAUDE.md
├── _SYSTEM/
│   ├── MASTER-CONTEXT.md      ← This file
│   ├── credentials.md
│   ├── changelog.md
│   ├── projects-index.md
│   ├── best-practices.md
│   └── infrastructure.md
│
└── _PROJECTS/
    ├── Website-Redesign - SR/
    ├── Kunden-Onboarding - SR/
    ├── Internes-Tool - SR/
    └── Mein-Erstes-Projekt - SR/
```

---

## Technical Infrastructure

### Server
| Property | Value |
|----------|-------|
| **IP** | 95.217.207.92 |
| **OS** | Ubuntu 24.04 LTS |
| **User** | root |
| **Firewall** | Ports 22, 80, 443 open |

### GitHub
| Property | Value |
|----------|-------|
| **Username** | srmamunmollah |
| **Repo** | Master-Knowledge (private) |

---

## Working Rules

All rules are in `CLAUDE.md` (read automatically).
Short version: Session start → git pull + read context. Session end → checklist + git push.

---

## Recent Changes

### 2026-07-17
- Built Telegram Boss Tasks app (see `_PROJECTS/Telegram-Boss-Tasks - SR/CONTEXT.md`)

### 2025-02-03
- Initial setup via Team-Onboarding completed
- Folder structure created, 4 test projects set up
- Server configured, Command Center deployed
