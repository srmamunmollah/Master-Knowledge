# CONTEXT.md - Telegram Boss Tasks

## What this is
A web app that turns Steve's boss's messages in a Telegram group into a tracked task list. No third-party cloud services, no external database, no paid APIs — runs on infrastructure Steve already owns.

## Status
✅ Built (2026-07-17) and ✅ deployed to the Hetzner server (2026-07-17), publicly reachable over HTTPS. Not yet connected to a real Telegram bot/group — needs `BOT_TOKEN`, `GROUP_CHAT_ID`, `BOSS_USER_ID` filled into the server's `.env` by Steve (see README.md for how to obtain them).

**Why it moved off the laptop:** the original design assumed Steve and his boss share a WiFi network. They don't — Steve is in Bangladesh, his boss is in Cyprus — so the app now runs on the always-on Hetzner VPS instead, reachable from anywhere.

## Live deployment
| Property | Value |
|---|---|
| **URL** | https://95-217-207-92.sslip.io |
| **Server** | Hetzner VPS, 95.217.207.92 (see `_SYSTEM/infrastructure.md`) |
| **App path on server** | `/root/websites/telegram-boss-tasks/` |
| **Runs as** | dedicated system user `tgtasks` (not root) |
| **Process manager** | systemd unit `telegram-boss-tasks.service` (`Restart=always`, enabled on boot) |
| **Reverse proxy** | nginx site `/etc/nginx/sites-available/telegram-boss-tasks`, proxies `95-217-207-92.sslip.io` → `127.0.0.1:3100` |
| **TLS** | Let's Encrypt cert via certbot for `95-217-207-92.sslip.io` (no domain purchase needed — sslip.io resolves the hostname to the server's own IP). Auto-renews. HTTP redirects to HTTPS. |
| **App port** | 3100, bound to `127.0.0.1` only (not reachable directly from the internet — confirmed via UFW deny-by-default and a direct external curl to port 3100 that fails) |
| **Logins** | `owner` / `boss` (viewer) — passwords generated with `openssl rand -hex 9`, stored only in the server's `.env` (`/root/websites/telegram-boss-tasks/.env`, `chmod 600`, owned by `tgtasks`). Not in git, not in this file. Steve has them from the deployment session. |

### Managing the live app
```bash
ssh root@95.217.207.92
systemctl status telegram-boss-tasks     # check it's running
systemctl restart telegram-boss-tasks    # after editing .env or redeploying code
journalctl -u telegram-boss-tasks -f     # tail logs (watch Telegram polling here)
```
To redeploy code after a local change: `rsync`/`scp` the changed file(s) to `/root/websites/telegram-boss-tasks/`, then `systemctl restart telegram-boss-tasks`. Run `npm install --omit=dev` on the server (not locally) if `package.json` changed, since `better-sqlite3` needs a native build for the server's architecture.

To fill in real Telegram credentials once Steve has them:
```bash
ssh root@95.217.207.92
nano /root/websites/telegram-boss-tasks/.env   # set BOT_TOKEN, GROUP_CHAT_ID, BOSS_USER_ID
systemctl restart telegram-boss-tasks
journalctl -u telegram-boss-tasks -f           # confirm "Starting long-polling worker..."
```

## Architecture
- **Backend**: Node.js + Express, in `server/`. Long-polls Telegram's `getUpdates` (no webhooks).
- **Storage**: `better-sqlite3`, single file `tasks.db` on the server (gitignored, created on first run).
- **Auth**: two hardcoded accounts via env vars — `owner` (full control, can change task status) and `viewer` (read-only, for the boss). Session-based via `express-session`.
- **Frontend**: plain HTML/CSS/JS in `public/`, no build step, polls `GET /api/tasks` every 10s.
- **Filtering**: only messages where `chat.id === GROUP_CHAT_ID` and `from.id === BOSS_USER_ID` become tasks; everyone else in the group is ignored. Dedup via stored `last_update_id` in the `meta` table.
- **Network binding**: `app.listen(PORT, HOST)` — `HOST` defaults to `0.0.0.0` (for the original same-LAN laptop use case) but is set to `127.0.0.1` in the server's `.env` since nginx handles public traffic there.

## Key files
- `server/index.js` — Express app, routes, session config, starts the poller
- `server/telegram.js` — long-polling worker, retries on error instead of crashing
- `server/auth.js` — hardcoded user lookup + role guards (`requireAuth`, `requireOwner`)
- `server/db.js` — SQLite schema + queries
- `server/seed.js` — inserts 3 placeholder tasks for UI testing before Telegram is wired up
- `public/` — login page + task list page + app.js

## How to run locally (original laptop/LAN mode)
See [README.md](README.md) for the original same-WiFi setup (BotFather steps, finding `GROUP_CHAT_ID`/`BOSS_USER_ID` via `getUpdates`, `.env` config, `npm install && npm start`). Superseded for cross-country use by the live server deployment above, but still works for local testing.

## Verified
**Local build (2026-07-17):** `npm install`/`npm start` clean, seed script works, owner status changes persist across restart, viewer read-only enforced both in UI and API (403/401).

**Server deployment (2026-07-17):**
- Node 20 + certbot installed on the Hetzner server; app files synced via rsync, dependencies rebuilt natively there
- systemd service running as unprivileged `tgtasks` user, enabled on boot, auto-restarts
- nginx reverse proxy + Let's Encrypt HTTPS working; HTTP→HTTPS redirect confirmed
- Confirmed app port 3100 is not directly reachable from the public internet (both by UFW policy and by binding to `127.0.0.1`)
- Confirmed login, `/api/health`, and `/api/tasks` all work over the public HTTPS URL

**Not yet tested:** an actual Telegram bot/group end-to-end — requires Steve to create the bot via BotFather and supply real `BOT_TOKEN`/`GROUP_CHAT_ID`/`BOSS_USER_ID` into the server's `.env`.

## Open TODOs
- Steve needs to create the Telegram bot via @BotFather and fill in the server's `.env` with real values.
- Once wired up, confirm a real message from the boss appears as a task within a few seconds, and that other group members' messages are ignored.
- Consider giving the boss a nicer bookmark/shortcut for `https://95-217-207-92.sslip.io` since it's not a memorable domain.
