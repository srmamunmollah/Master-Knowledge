require('dotenv').config();
const path = require('path');
const express = require('express');
const session = require('express-session');

const { listTasks, updateTaskStatus } = require('./db');
const { verifyLogin, requireAuth, requireOwner } = require('./auth');
const { startPolling } = require('./telegram');

const app = express();
const PORT = process.env.PORT || 3000;
const VALID_STATUSES = ['todo', 'in_progress', 'done'];

app.use(express.json());
app.use(
  session({
    secret: process.env.SESSION_SECRET || 'dev-secret-change-me',
    resave: false,
    saveUninitialized: false,
    cookie: { maxAge: 1000 * 60 * 60 * 24 * 7 },
  })
);

app.get('/api/health', (req, res) => res.json({ ok: true }));

app.post('/api/login', (req, res) => {
  const { username, password } = req.body || {};
  const user = verifyLogin(username, password);
  if (!user) return res.status(401).json({ error: 'Invalid credentials' });
  req.session.user = user;
  res.json(user);
});

app.post('/api/logout', (req, res) => {
  req.session.destroy(() => res.json({ ok: true }));
});

app.get('/api/me', requireAuth, (req, res) => {
  res.json(req.session.user);
});

app.get('/api/tasks', requireAuth, (req, res) => {
  res.json(listTasks());
});

app.patch('/api/tasks/:id', requireOwner, (req, res) => {
  const { status } = req.body || {};
  if (!VALID_STATUSES.includes(status)) {
    return res.status(400).json({ error: `status must be one of: ${VALID_STATUSES.join(', ')}` });
  }
  const result = updateTaskStatus(req.params.id, status);
  if (result.changes === 0) return res.status(404).json({ error: 'Task not found' });
  res.json({ ok: true });
});

app.use(express.static(path.join(__dirname, '..', 'public')));

// Default 0.0.0.0 so the app is reachable from other devices on the same LAN
// (the local/laptop setup this app was originally built for). When running
// behind a reverse proxy (see the server deployment), set HOST=127.0.0.1
// in .env so the app is only reachable through the proxy.
const HOST = process.env.HOST || '0.0.0.0';

app.listen(PORT, HOST, () => {
  console.log(`Server running at http://${HOST}:${PORT}`);
});

startPolling();
