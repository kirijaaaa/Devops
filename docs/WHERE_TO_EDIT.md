# Where to Edit for Visible Changes

**Most content is in ONE file:** `app.py`  
After saving, refresh browser at http://localhost:5000 (with `python app.py` running).

---

## Quick map: what you see → where to edit

| What you see on website | Section in `app.py` | Line area |
|-------------------------|---------------------|-----------|
| **Name** on Home & Footer | `PERSONAL` → `"name"`, `"first_name"` | ~6–7 |
| **Job title** under name | `PERSONAL` → `"role"` | ~8 |
| **Tagline** (sentence below role) | `PERSONAL` → `"tagline"` | ~9 |
| **Email, Phone, Location** (Contact) | `PERSONAL` → `"email"`, `"phone"`, `"location"` | ~10–12 |
| **Who I Am** paragraph | `ABOUT` → `"summary"` | ~28–34 |
| **About bullet points** (4 boxes) | `ABOUT` → `"highlights"` | ~34–39 |
| **Skill bars** | `SKILLS` list | ~42–51 |
| **Education / College** | `EDUCATION` first item | ~53–63 |
| **Higher Secondary / SVM** | `EDUCATION` second item | ~64–71 |
| **Project cards** | `PROJECTS` list | ~73–118 |

---

## Design / layout (optional)

| Change | File |
|--------|------|
| Colors, fonts, spacing | `static/css/style.css` |
| Page structure (sections order) | `templates/index.html` |
| Buttons, animations | `static/js/main.js` |
| Resume PDF download | Replace `static/resume.pdf` |
| Favicon | `static/images/favicon.svg` |

---

## CI/CD (only if you change name on homepage)

| File | What to update |
|------|----------------|
| `.github/workflows/ci-cd.yml` | Line with `assert b'KIRIJA'` — must match name in `app.py` |

---

## Steps after every edit

1. Save `app.py`
2. If Flask is running, refresh browser (Ctrl+F5)
3. If not running: `python app.py` then open http://localhost:5000
4. For live site: `git add .` → `git commit -m "message"` → `git push`

---

## Your current details (already set)

- **Name:** KIRIJA  
- **Role:** B.Tech Information Technology Student  
- **Location:** Coimbatore, Tamil Nadu, India  
- **College:** Kumaraguru College of Technology, Coimbatore, Tamil Nadu  
- **HSC:** Bio Maths, SVM, 2020–2022 (Biology, not Computer Science)  

Edit `app.py` anytime to update phone, email, CGPA, or project links.
