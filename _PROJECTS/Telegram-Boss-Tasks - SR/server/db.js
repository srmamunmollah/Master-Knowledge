const path = require('path');
const Database = require('better-sqlite3');

const DB_PATH = path.join(__dirname, '..', 'tasks.db');
const db = new Database(DB_PATH);

db.pragma('journal_mode = WAL');

db.exec(`
  CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    message_text TEXT NOT NULL,
    created_at TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'todo',
    telegram_message_id INTEGER,
    telegram_update_id INTEGER UNIQUE
  );

  CREATE TABLE IF NOT EXISTS meta (
    key TEXT PRIMARY KEY,
    value TEXT
  );
`);

function getMeta(key) {
  const row = db.prepare('SELECT value FROM meta WHERE key = ?').get(key);
  return row ? row.value : null;
}

function setMeta(key, value) {
  db.prepare(
    `INSERT INTO meta (key, value) VALUES (?, ?)
     ON CONFLICT(key) DO UPDATE SET value = excluded.value`
  ).run(key, value);
}

function insertTask({ messageText, createdAt, telegramMessageId, telegramUpdateId }) {
  return db
    .prepare(
      `INSERT OR IGNORE INTO tasks (message_text, created_at, status, telegram_message_id, telegram_update_id)
       VALUES (?, ?, 'todo', ?, ?)`
    )
    .run(messageText, createdAt, telegramMessageId, telegramUpdateId);
}

function listTasks() {
  return db.prepare('SELECT * FROM tasks ORDER BY id DESC').all();
}

function updateTaskStatus(id, status) {
  return db.prepare('UPDATE tasks SET status = ? WHERE id = ?').run(status, id);
}

module.exports = { db, getMeta, setMeta, insertTask, listTasks, updateTaskStatus };
