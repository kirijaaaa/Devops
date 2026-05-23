# Cloud-Native CI/CD Pipeline for Automated Portfolio Deployment

**Final-Year Project** — Flask portfolio website with automated CI/CD using **Docker**, **GitHub Actions**, and **Render**.

## Architecture Flow

```
Portfolio (Flask) → GitHub → GitHub Actions → Docker → Render → Live Website
```

## Project Structure

```
project-folder/
├── app.py                    # Flask application
├── requirements.txt          # Python dependencies
├── Dockerfile                # Container image
├── docker-compose.yml
├── render.yaml               # Render Blueprint
├── .github/
│   └── workflows/
│       └── ci-cd.yml         # CI/CD pipeline
├── templates/
│   └── index.html            # Portfolio page
└── static/
    ├── css/style.css
    ├── js/main.js
    ├── images/favicon.svg
    └── resume.pdf
```

## Quick Start

### Local Development

```bash
pip install -r requirements.txt
python app.py
```

Open http://localhost:5000

### Docker

```bash
docker build -t portfolio-app .
docker run -p 5000:5000 portfolio-app
```

### Docker Compose

```bash
docker compose up --build
```

## CI/CD Pipeline

**File:** `.github/workflows/ci-cd.yml`

| Step | Action |
|------|--------|
| Trigger | Push / PR to `main` |
| Install | `pip install -r requirements.txt` |
| Test | Flask test client validates `/` returns 200 |
| Docker | Build image + health check on port 5000 |
| Deploy | Render deploy hook (main branch only) |

## Deploy to Render

1. Push repo to GitHub
2. [render.com](https://render.com) → **New Web Service** → Connect repo
3. Runtime: **Docker** · Port: **5000**
4. Add GitHub secret `RENDER_DEPLOY_HOOK` (from Render → Settings → Deploy Hook)

## Push to GitHub

```bash
git init
git add .
git commit -m "Initial Commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/portfolio-cicd.git
git push -u origin main
```

## Customize

Edit portfolio content in **`app.py`** (PERSONAL, SKILLS, PROJECTS, etc.).

Replace **`static/resume.pdf`** with your CV.

## Documentation

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)
- [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md)
- [docs/PROJECT_REPORT.md](docs/PROJECT_REPORT.md)

## Technology Stack

| Layer | Technology |
|-------|------------|
| Web App | Flask 3.0, Jinja2 |
| Server | Gunicorn |
| Container | Docker (Python 3.11) |
| CI/CD | GitHub Actions |
| Cloud | Render |
