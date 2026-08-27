# Best Practices - Proven Solutions

Solutions that have worked well are documented here.
Format: Problem → Solution → Why it works.

---

## Server & Deployment

### Deploy website to server
```bash
scp file.html root@95.217.207.92:/path/to/destination/
```
Works reliably for individual files.

### Set up SSL certificate
```bash
certbot --nginx -d yourdomain.com
```
Free SSL from Let's Encrypt. Renews automatically.

### Get HTTPS on a server with no domain name
**Problem:** Let's Encrypt needs a real hostname to issue a cert, but not every server/project has a purchased domain.
**Solution:** Use a free wildcard-DNS service like `sslip.io` — `<ip-with-dashes>.sslip.io` (e.g. `95-217-207-92.sslip.io`) automatically resolves to that IP with no signup, and it's a real DNS name so certbot issues a normal trusted cert for it (`certbot --nginx -d 95-217-207-92.sslip.io`).
**Why it works:** sslip.io just runs authoritative DNS that parses the IP out of the hostname and returns it — Let's Encrypt's domain validation only checks that the hostname resolves and that you control the server behind it, both of which are true. `nip.io` works the same way.
**Used for:** Telegram-Boss-Tasks deployment (`_PROJECTS/Telegram-Boss-Tasks - SR/`), reachable at `https://95-217-207-92.sslip.io`.

### Expose a Node app safely behind nginx
**Problem:** `app.listen(PORT)` binds to `0.0.0.0` by default — directly reachable from the internet, bypassing nginx and TLS entirely, if the firewall ever changes.
**Solution:** Explicitly bind to `127.0.0.1` (`app.listen(PORT, '127.0.0.1', ...)`) when the app sits behind an nginx reverse proxy, and don't rely on the firewall alone.
**Why it works:** defense in depth — even if a UFW rule is loosened later, the app itself is unreachable except through the proxy.

---

## Git Workflow

### Daily routine
1. `git pull origin main` (Start)
2. Work
3. `git add . && git commit -m "Description" && git push origin main` (End)

### Avoid conflicts
- Always pull before you start working
- Always push at the end
- Don't edit the same file in multiple places simultaneously

---

## Adding a New Best Practice

When you've solved a problem (>20 min debugging), document it here:
1. **Problem:** What was the problem?
2. **Solution:** What worked?
3. **Why:** Why does it work?

---

*Last updated: 2025-02-03*
