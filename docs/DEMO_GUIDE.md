# Live Project Demo Guide (For Staff Presentation)

**Duration:** 10–15 minutes  
**Goal:** Show code change → local test → Git push → CI/CD pipeline → live site update

---

## Before the presentation (prepare once)

| Check | How |
|-------|-----|
| Flask runs locally | `python app.py` → http://localhost:5000 |
| Code on GitHub | Repo pushed to `main` |
| Render connected | Web Service linked to same repo, Auto-Deploy ON |
| GitHub Actions enabled | Push once before demo so staff see green workflow history |
| Browser tabs ready | Tab 1: localhost:5000, Tab 2: GitHub repo, Tab 3: Actions, Tab 4: Render live URL |

**Replace demo values with YOUR real name** in `app.py` before the presentation.

---

## Demo Change #1 — Name & role (easiest, recommended)

**What staff will see:** Hero section text changes on website.

**Where:** `app.py` → `PERSONAL` dictionary (lines 5–16)

**Change this:**
```python
"name": "Alex Morgan",
"first_name": "Alex",
"role": "Full Stack Developer & DevOps Engineer",
"tagline": "Building scalable cloud-native applications with modern CI/CD pipelines.",
```

**To this (use your name):**
```python
"name": "Your Full Name",
"first_name": "YourFirstName",
"role": "B.Tech CSE Student | DevOps Project",
"tagline": "Live demo: automated CI/CD from GitHub to Render — updated just now!",
```

**Also update CI test** in `.github/workflows/ci-cd.yml` line 36:
```python
assert b'Your Full Name' in r.data
```
(Change `Alex Morgan` to your name so pipeline test still passes.)

---

## Demo Change #2 — Add a visible badge on homepage

**Where:** `templates/index.html` → Hero section (around line 54)

**Find:**
```html
<span class="badge">Available for opportunities</span>
```

**Change to:**
```html
<span class="badge">✓ CI/CD Demo — Deployed {{ "now" }}</span>
```
Better with Flask — add in `app.py` and pass to template, OR simply:
```html
<span class="badge">✓ Live CI/CD Demo — May 2026</span>
```

---

## Demo Change #3 — Add one new skill (shows data-driven app)

**Where:** `app.py` → `SKILLS` list

**Add at the end:**
```python
{"name": "CI/CD Pipelines", "level": 95, "category": "DevOps"},
```

Refresh browser → Skills section shows new bar.

---

## Demo Change #4 — Add a project card (optional)

**Where:** `app.py` → `PROJECTS` list

**Add:**
```python
{
    "title": "Live Staff Demo Project",
    "description": "Demonstrated automated deployment using Flask, Docker, GitHub Actions, and Render.",
    "tech": ["Flask", "Docker", "GitHub Actions"],
    "github": "https://github.com/YOUR_USERNAME/YOUR_REPO",
    "live": "#home",
    "featured": True,
},
```

---

## Step-by-step presentation flow

### PART 1 — Explain the project (2 min)

**Say:**
> "This is a portfolio website built with Flask. The main focus is the DevOps pipeline: when I change code and push to GitHub, GitHub Actions automatically tests, builds a Docker image, and Render deploys the live website."

**Show folder structure:**
```
app.py          → Backend
templates/      → HTML
static/         → CSS, JS
Dockerfile      → Container
.github/workflows/ci-cd.yml → Automation
```

---

### PART 2 — Show current live site (1 min)

1. Open **http://localhost:5000** (or Render URL if already deployed)
2. Scroll: Home → About → Skills → Projects → Contact
3. **Say:** "This is the application users see."

---

### PART 3 — Make a code change LIVE (3 min)

1. Open **`app.py`** in VS Code / Cursor
2. Change **`PERSONAL["tagline"]`** to something with today's date:
   ```python
   "tagline": "Staff demo — automated deploy test on 25 May 2026",
   ```
3. Update **`ci-cd.yml`** test line to match your name (if you changed name)
4. **Save** the file

---

### PART 4 — Test locally (2 min)

**Terminal:**
```powershell
cd "c:\Users\kkiri\OneDrive\Attachments\Desktop\Devops"
python app.py
```

1. Open **http://localhost:5000**
2. **Refresh** (Ctrl+F5) — staff see new tagline
3. **Say:** "First we verify the change works on my machine before deploying."

**Optional — show Docker locally:**
```powershell
docker build -t portfolio-app .
docker run -p 5000:5000 portfolio-app
```
**Say:** "Same app runs inside Docker — same as production."

---

### PART 5 — Push to GitHub → trigger CI/CD (4 min)

**Terminal (new tab or stop Flask with Ctrl+C):**
```powershell
git status
git add app.py
git commit -m "Demo: update tagline for staff presentation"
git push origin main
```

**Then open GitHub in browser:**

1. Go to your **repository**
2. Click **Actions** tab
3. Click the **latest workflow run** (yellow = running, green = success)
4. **Say and point:**
   - "Checkout code"
   - "Install dependencies"
   - "Run Flask App Test" — proves app works
   - "Build Docker image"
   - "Validate container" — health check on port 5000
   - "Deploy to Render" (if secret set) OR Render auto-deploys separately

**Staff should see:** Pipeline running in real time → all steps green.

---

### PART 6 — Show live deployment (2 min)

1. Open **Render dashboard** → your service → **Events** or **Logs**
2. Show **new deploy** started after git push
3. When done, open **live URL** (e.g. `https://portfolio-cicd.onrender.com`)
4. **Refresh** — new tagline visible
5. **Say:** "Code change on GitHub became a live website without manual upload."

---

## What to say when staff ask questions

| Question | Answer |
|----------|--------|
| What did you change? | Updated content in `app.py` — Flask sends data to HTML template |
| How does it deploy? | Git push → GitHub Actions → Docker build → Render hosts container |
| Why Docker? | Same environment everywhere — no "works on my PC only" |
| Is secret required? | No — Render Auto-Deploy from GitHub is enough for demo |
| What if test fails? | Pipeline stops — broken code does not deploy |

---

## Quick demo script (one small change only)

If time is short, do **only this**:

1. Change `tagline` in `app.py`
2. `python app.py` → show browser
3. `git add .` → `git commit -m "demo update"` → `git push`
4. Show GitHub Actions green
5. Show Render / live URL updated

**Total time: ~8 minutes**

---

## Troubleshooting during demo

| Problem | Fix |
|---------|-----|
| Connection refused | Run `python app.py` — use port **5000** |
| Actions failed on name test | Update `assert b'Your Name'` in `ci-cd.yml` |
| Render not updating | Check Auto-Deploy ON; wait 3–5 min; hard refresh |
| Git push rejected | `git pull` first, then push |

---

## Checklist on presentation day

- [ ] Laptop charged, internet working
- [ ] GitHub logged in
- [ ] Render logged in
- [ ] `python app.py` tested morning of presentation
- [ ] One demo change prepared (tagline or name)
- [ ] `ci-cd.yml` test string matches your name
- [ ] Live Render URL written on slide / paper

---

## Files summary — where to change what

| What to change | File | Section |
|----------------|------|---------|
| Name, email, role | `app.py` | `PERSONAL` |
| About text | `app.py` | `ABOUT` |
| Skills | `app.py` | `SKILLS` |
| Projects | `app.py` | `PROJECTS` |
| Page layout / HTML | `templates/index.html` |
| Colors / design | `static/css/style.css` |
| CI test assertion | `.github/workflows/ci-cd.yml` | Flask test step |
| Docker config | `Dockerfile` |

Good luck with your presentation.
