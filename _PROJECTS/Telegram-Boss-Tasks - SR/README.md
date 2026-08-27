# Telegram Boss Tasks

Turns your boss's messages in a Telegram group into a task list you can track. No third-party cloud services, no external database, no paid APIs.

> **This app is live** at **https://95-217-207-92.sslip.io**, running on the Hetzner server rather than a laptop — the original same-WiFi design didn't work once Steve (Bangladesh) and his boss (Cyprus) needed access from different countries. See [CONTEXT.md](CONTEXT.md) for the live deployment details (systemd service, nginx, HTTPS cert, how to redeploy). The instructions below describe the original laptop/LAN setup, which still works for local testing.

## How it works

- A small Node.js server long-polls the Telegram Bot API for new messages in one group chat.
- Messages sent by your boss's Telegram account are saved as tasks in a local SQLite file (`tasks.db`).
- A plain HTML/JS page (served by the same server) shows the task list. You can change status; your boss can only view.
- Everything runs on your local network — you and your boss just need to be on the same WiFi to check the site, and your laptop needs to be on for the bot to catch new messages.

## 1. Create the Telegram bot

1. Open Telegram, message **@BotFather**.
2. Send `/newbot` and follow the prompts (pick a name and a username ending in `bot`).
3. BotFather replies with a token that looks like `123456789:AAExampleTokenValue`. Copy it — this is `BOT_TOKEN`.

## 2. Create the group and find the IDs

1. Create a Telegram group. Add your boss and add your new bot to it.
2. Send any message in the group (from any member).
3. In a browser, open:
   ```
   https://api.telegram.org/bot<BOT_TOKEN>/getUpdates
   ```
   (replace `<BOT_TOKEN>` with your real token).
4. In the JSON response, find the message you just sent. You'll see something like:
   ```json
   {
     "message": {
       "message_id": 5,
       "from": { "id": 987654321, "first_name": "..." },
       "chat": { "id": -1001234567890, "title": "..." },
       "text": "hello"
     }
   }
   ```
   - `chat.id` → this is your `GROUP_CHAT_ID` (group chat ids are usually negative numbers).
   - To get your **boss's** `user_id`, have your boss send a message in the group, then refresh `getUpdates` and read `from.id` on their message → this is `BOSS_USER_ID`.

If `getUpdates` returns an empty `result: []`, send a fresh message in the group and reload the URL — Telegram only returns unconfirmed updates.

## 3. Configure the app

```bash
cp .env.example .env
```

Edit `.env` and fill in:

| Variable | Value |
|---|---|
| `BOT_TOKEN` | from step 1 |
| `GROUP_CHAT_ID` | from step 2 |
| `BOSS_USER_ID` | from step 2 |
| `SESSION_SECRET` | any long random string |
| `OWNER_USERNAME` / `OWNER_PASSWORD` | your login (full control) |
| `VIEWER_USERNAME` / `VIEWER_PASSWORD` | your boss's login (view-only) |

You can leave `BOT_TOKEN`/`GROUP_CHAT_ID`/`BOSS_USER_ID` blank at first to test the UI before wiring up the real bot (see step 5).

## 4. Install and run

```bash
npm install
npm start
```

You'll see:

```
Server running at http://localhost:3000
```

Open `http://localhost:3000/login.html` in your browser and log in with the owner credentials from `.env`.

### Access from another device on the same network

Find your laptop's local IP (e.g. `ipconfig getifaddr en0` on macOS, or check System Settings → Network), then open:

```
http://<your-laptop-ip>:3000/login.html
```

from your boss's phone/laptop, as long as it's on the same WiFi. Your boss logs in with the viewer credentials.

## 5. Test the UI before connecting Telegram

Before filling in the Telegram credentials, you can seed some placeholder tasks to confirm the UI works end-to-end:

```bash
npm run seed
```

This inserts 3 sample tasks directly into `tasks.db`. Start the server (`npm start`), log in, and confirm you can see them and (as owner) change their status.

## 6. Go live

Once `.env` has real `BOT_TOKEN`, `GROUP_CHAT_ID`, and `BOSS_USER_ID` values, restart the server (`npm start`). The console will log:

```
[telegram] Starting long-polling worker...
```

Send a test message as your boss in the group — a new task should appear on the site within a few seconds. Messages from anyone else in the group are ignored.

## Notes

- Tasks and login sessions persist in `tasks.db` on disk — restarting the server does not lose data.
- If the Telegram API is briefly unreachable, the worker logs the error and retries automatically instead of crashing.
- The bot must remain a member of the group and the laptop must stay on and running `npm start` for new messages to be picked up.
