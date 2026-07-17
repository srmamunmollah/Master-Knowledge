const { getMeta, setMeta, insertTask } = require('./db');

const BOT_TOKEN = process.env.BOT_TOKEN;
const GROUP_CHAT_ID = process.env.GROUP_CHAT_ID;
const BOSS_USER_ID = process.env.BOSS_USER_ID;

const API_BASE = BOT_TOKEN ? `https://api.telegram.org/bot${BOT_TOKEN}` : null;
const RETRY_DELAY_MS = 5000;

let polling = false;

async function fetchUpdates(offset) {
  const url = `${API_BASE}/getUpdates?timeout=30${offset != null ? `&offset=${offset}` : ''}`;
  const res = await fetch(url);
  if (!res.ok) {
    throw new Error(`Telegram API HTTP error: ${res.status} ${res.statusText}`);
  }
  const data = await res.json();
  if (!data.ok) {
    throw new Error(`Telegram API returned an error: ${JSON.stringify(data)}`);
  }
  return data.result;
}

function processUpdate(update) {
  const msg = update.message;
  const isFromBoss =
    msg &&
    msg.chat &&
    String(msg.chat.id) === String(GROUP_CHAT_ID) &&
    msg.from &&
    String(msg.from.id) === String(BOSS_USER_ID) &&
    typeof msg.text === 'string' &&
    msg.text.length > 0;

  if (isFromBoss) {
    insertTask({
      messageText: msg.text,
      createdAt: new Date(msg.date * 1000).toISOString(),
      telegramMessageId: msg.message_id,
      telegramUpdateId: update.update_id,
    });
    console.log(`[telegram] Created task from message: "${msg.text.slice(0, 60)}"`);
  }
}

async function startPolling() {
  if (!BOT_TOKEN || !GROUP_CHAT_ID || !BOSS_USER_ID) {
    console.warn(
      '[telegram] BOT_TOKEN, GROUP_CHAT_ID, or BOSS_USER_ID not set — polling disabled. Running in UI-only mode.'
    );
    return;
  }

  polling = true;
  const storedOffset = getMeta('last_update_id');
  let offset = storedOffset != null ? parseInt(storedOffset, 10) + 1 : undefined;

  console.log('[telegram] Starting long-polling worker...');

  while (polling) {
    try {
      const updates = await fetchUpdates(offset);
      for (const update of updates) {
        processUpdate(update);
        offset = update.update_id + 1;
        setMeta('last_update_id', String(update.update_id));
      }
    } catch (err) {
      console.error('[telegram] Polling error, will retry:', err.message);
      await new Promise((resolve) => setTimeout(resolve, RETRY_DELAY_MS));
    }
  }
}

function stopPolling() {
  polling = false;
}

module.exports = { startPolling, stopPolling };
