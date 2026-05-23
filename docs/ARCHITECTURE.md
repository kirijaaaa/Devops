# System Architecture (Flask)

## Flow

```
Developer → git push → GitHub → GitHub Actions → Docker → Render → Live Website
```

## Stack

| Layer | Technology |
|-------|------------|
| Application | Flask 3.0 (Python) |
| Templates | Jinja2 (`templates/index.html`) |
| Static assets | CSS, JS, images in `static/` |
| Production server | Gunicorn (port 5000) |
| Container | Docker (python:3.11-slim) |
| CI/CD | GitHub Actions (`.github/workflows/ci-cd.yml`) |
| Cloud | Render |

## Request Flow

1. User visits `/`
2. Flask `home()` renders `templates/index.html` with portfolio data from `app.py`
3. Static files served from `/static/css`, `/static/js`, `/static/images`
4. Resume download via `/resume.pdf` route

## CI/CD Jobs

1. **build** — Install deps → Flask test → Docker build → container health check
2. **deploy** — POST Render deploy hook (main branch only)
