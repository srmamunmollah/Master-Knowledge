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
