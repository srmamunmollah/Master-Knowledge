# CONTEXT.md - Telegram Boss Tasks

## What this is
A local-only web app that turns Steve's boss's messages in a Telegram group into a tracked task list. No cloud services, no external database, no paid APIs.

## Status
✅ Built and verified (2026-07-17). Not yet connected to a real Telegram bot/group — needs `BOT_TOKEN`, `GROUP_CHAT_ID`, `BOSS_USER_ID` filled into `.env` by Steve (see README.md for how to obtain them).

## Architecture
- **Backend**: Node.js + Express, in `server/`. Long-polls Telegram's `getUpdates` (no webhooks, no tunneling needed — LAN only).
- **Storage**: `better-sqlite3`, single file `tasks.db` (gitignored, created on first run).
- **Auth**: two hardcoded accounts via env vars — `owner` (full control, can change task status) and `viewer` (read-only, for the boss). Session-based via `express-session`.
- **Frontend**: plain HTML/CSS/JS in `public/`, no build step, polls `GET /api/tasks` every 10s.
- **Filtering**: only messages where `chat.id === GROUP_CHAT_ID` and `from.id === BOSS_USER_ID` become tasks; everyone else in the group is ignored. Dedup via stored `last_update_id` in the `meta` table.

## Key files
- `server/index.js` — Express app, routes, session config, starts the poller
- `server/telegram.js` — long-polling worker, retries on error instead of crashing
- `server/auth.js` — hardcoded user lookup + role guards (`requireAuth`, `requireOwner`)
- `server/db.js` — SQLite schema + queries
- `server/seed.js` — inserts 3 placeholder tasks for UI testing before Telegram is wired up
- `public/` — login page + task list page + app.js

## How to run
See [README.md](README.md) for full setup (BotFather steps, finding `GROUP_CHAT_ID`/`BOSS_USER_ID` via `getUpdates`, `.env` config, `npm install && npm start`).

## Verified during build (2026-07-17)
- `npm install` and `npm start` work cleanly (tested on port 3101 since 3000 was occupied by an unrelated local process — no fixed port dependency).
- `npm run seed` inserts placeholder tasks so the UI can be checked before real Telegram credentials exist.
- Owner login can PATCH task status; change persists in `tasks.db` across a server restart.
- Viewer login can read tasks but the UI hides the Actions column, and the API returns 403 on PATCH for viewer, 401 for no session.
- Not yet tested: an actual Telegram bot/group end-to-end (requires Steve to create the bot via BotFather and supply real `BOT_TOKEN`/`GROUP_CHAT_ID`/`BOSS_USER_ID`).

## Open TODOs
- Steve needs to create the Telegram bot via @BotFather and fill in real `.env` values.
- Once wired up, confirm a real message from the boss appears as a task within a few seconds, and that other group members' messages are ignored.
- Decide whether this should be deployed to the Hetzner server (`_SYSTEM/infrastructure.md` / `_SYSTEM/credentials.md`) later, or stay laptop-only as originally scoped (currently laptop-only by design).
