# Deployment Guide (Flask)

## Local

```bash
pip install -r requirements.txt
python app.py
```

Visit http://localhost:5000

## Docker

```bash
docker build -t portfolio-app .
docker run -p 5000:5000 portfolio-app
```

## Render

1. Push to GitHub (`main` branch)
2. Render → **New Web Service** → Connect repository
3. **Runtime:** Docker
4. **Port:** 5000
5. Deploy

### Auto-deploy via GitHub Actions

Add secret `RENDER_DEPLOY_HOOK` in GitHub repo settings (value from Render → Deploy Hook URL).

## GitHub Push

```bash
git init
git add .
git commit -m "Initial Commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```
