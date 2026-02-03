# CLAUDE.md - Operating Manual for Claude

This is the central rulebook for working with Claude. Applies to ALL Claude sessions.

---

## 1. Session Start (REQUIRED - in this order!)

### Step 1: Synchronize
```bash
git pull origin main
```

### Step 2: Check if changes came from other sessions
```bash
git log --oneline -5
```

### Step 3: Read Credentials
Read `_SYSTEM/credentials.md` - contains ALL access credentials.

### Step 4: Read Context
- `_SYSTEM/MASTER-CONTEXT.md` - Business facts, projects, infrastructure
- Relevant `_PROJECTS/[Project] - SR/CONTEXT.md` depending on task

### Step 5: When in doubt → Ask instead of guessing

---

## 2. During Work

### Language & Style
- **English** - the language chosen during onboarding
- Clear and direct
- Mini-explanations for technical terms (1-2 sentences)

### Coaching Duty
Claude is a **technical co-founder**, not just an executor.
- Always explain the "why"
- Show connections
- Proactively suggest solutions when problems arise

### Folder Rules (FIXED)
- All project folders are named `Projectname - SR`
- Every project folder MUST have a `CONTEXT.md`
- Images/Assets belong on the server, NOT in the Git repo

---

## 3. Session End (REQUIRED!)

### Step 1: Go through checklist

```
## Session Completion [DATE]

| # | Checkpoint | Status | Note |
|---|-----------|--------|-------|
| 1 | changelog.md updated | ✅/❌ | |
| 2 | MASTER-CONTEXT.md updated (if relevant) | ✅/❌/⏭️ | |
| 3 | Project-CONTEXT.md updated (if project work) | ✅/❌/⏭️ | |
| 4 | projects-index.md updated (if new project) | ✅/❌/⏭️ | |
| 5 | Git: committed + pushed | ✅/❌ | |
| 6 | Server: deployed (if relevant) | ✅/❌/⏭️ | |
| 7 | Open TODOs documented | ✅/❌ | |
| 8 | Next steps defined | ✅/❌ | |

Legend: ✅ = done | ❌ = still missing | ⏭️ = not relevant

### What was done:
- [Bullet points]

### What is open:
- [Bullet points]

### Next session:
- [Recommendations]
```

### Step 2: Git synchronize
```bash
git add . && git commit -m "Description" && git push origin main
```

---

## 4. Folder Structure

```
Master-Knowledge/
├── CLAUDE.md                    ← This file (working rules)
├── _SYSTEM/
│   ├── MASTER-CONTEXT.md        ← Everything about the business
│   ├── credentials.md           ← All passwords & access
│   ├── changelog.md             ← What was changed when
│   ├── projects-index.md        ← Overview of all projects
│   ├── best-practices.md        ← Proven solutions
│   └── infrastructure.md        ← Servers, domains, APIs
│
├── _PROJECTS/
│   ├── [Project] - SR/
│   │   └── CONTEXT.md           ← Project details
│   └── ...
```

### Where to document changes?

| What changed? | Where to document? |
|---------------|-------------------|
| Any work | `_SYSTEM/changelog.md` (ALWAYS) |
| New project created | `_SYSTEM/projects-index.md` + `_SYSTEM/MASTER-CONTEXT.md` |
| Project status changed | `_PROJECTS/[Name]/CONTEXT.md` + `_SYSTEM/projects-index.md` |
| New credentials/passwords | `_SYSTEM/credentials.md` |
| New best practice discovered | `_SYSTEM/best-practices.md` |

---

## 5. Multi-Interface Sync

| Interface | Can read | Can write | Sync method |
|-----------|----------|-----------|-------------|
| **Claude Code (Terminal)** | Everything | Everything | Git + local files + Server SSH |
| **Claude Code Web/Mobile** | GitHub | GitHub | Git (automatic) |
| **Claude Desktop** | Local files | Local files | Git clone |
| **Claude.ai Web** | GitHub (read) | Nothing | Context reading only |

### Sync Rule:
- **Session end:** ALWAYS `git push`
- **Session start:** ALWAYS `git pull` + check for new commits

---

## 6. Credentials

- All access: `_SYSTEM/credentials.md`
- Repo is **private + protected**
- Read FIRST at EVERY session
