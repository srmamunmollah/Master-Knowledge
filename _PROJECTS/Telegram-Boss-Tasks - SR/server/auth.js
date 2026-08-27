const crypto = require('crypto');

function buildUsers() {
  const users = {};
  const ownerUsername = process.env.OWNER_USERNAME || 'owner';
  const viewerUsername = process.env.VIEWER_USERNAME || 'viewer';

  users[ownerUsername] = { password: process.env.OWNER_PASSWORD || 'changeme', role: 'owner' };
  users[viewerUsername] = { password: process.env.VIEWER_PASSWORD || 'changeme', role: 'viewer' };

  return users;
}

const USERS = buildUsers();

function safeCompare(a, b) {
  const bufA = Buffer.from(String(a));
  const bufB = Buffer.from(String(b));
  if (bufA.length !== bufB.length) return false;
  return crypto.timingSafeEqual(bufA, bufB);
}

function verifyLogin(username, password) {
  const user = USERS[username];
  if (!user || !password) return null;
  if (!safeCompare(user.password, password)) return null;
  return { username, role: user.role };
}

function requireAuth(req, res, next) {
  if (!req.session.user) return res.status(401).json({ error: 'Not authenticated' });
  next();
}

function requireOwner(req, res, next) {
  if (!req.session.user) return res.status(401).json({ error: 'Not authenticated' });
  if (req.session.user.role !== 'owner') return res.status(403).json({ error: 'Owner access required' });
  next();
}

module.exports = { verifyLogin, requireAuth, requireOwner };
