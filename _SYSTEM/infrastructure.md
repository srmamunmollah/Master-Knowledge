# Infrastructure

---

## Server

### Workspace Server
| Property | Value |
|----------|-------|
| **IP** | 95.217.207.92 |
| **OS** | Ubuntu 24.04 LTS |
| **Provider** | Hetzner Cloud |
| **User** | root |

**Important paths:**
| Path | Purpose |
|------|---------|
| `/root/websites/` | All websites |
| `/root/websites/command-center/` | Command Center Dashboard |
| `/etc/nginx/sites-available/` | Nginx configurations |

**Firewall (UFW):** Ports 22, 80, 443, 8080 open

---

## GitHub

| Property | Value |
|----------|-------|
| **Username** | srmamunmollah |
| **Repo** | Master-Knowledge (private) |

---

## Services

### Telegram Boss Tasks
| Property | Value |
|---|---|
| **URL** | https://95-217-207-92.sslip.io |
| **Path** | `/root/websites/telegram-boss-tasks/` |
| **Runs as** | systemd service `telegram-boss-tasks.service`, user `tgtasks` |
| **Internal port** | 3100 (127.0.0.1 only, proxied by nginx) |
| **Nginx config** | `/etc/nginx/sites-available/telegram-boss-tasks` |
| **TLS** | Let's Encrypt via certbot, auto-renews |
| **Details** | `_PROJECTS/Telegram-Boss-Tasks - SR/CONTEXT.md` |

---

*Last updated: 2026-07-17*
