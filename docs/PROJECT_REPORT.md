# Project Report

## Cloud-Native CI/CD Pipeline for Automated Portfolio Deployment Using Docker and GitHub Actions

**Submitted by:** [Your Name]  
**Department:** Computer Science / Information Technology  
**Academic Year:** 2025–2026  
**Guide:** [Guide Name]

---

## 1. Introduction

Modern software delivery demands automation across the entire lifecycle—from code commit to production deployment. This project demonstrates a complete **DevOps pipeline** that automatically builds, tests, containerizes, and deploys a professional portfolio website whenever changes are pushed to a Git repository.

The solution integrates industry-standard tools: **React** for the frontend, **Docker** for containerization, **GitHub Actions** for CI/CD, and **Render** for cloud hosting.

---

## 2. Problem Statement

Traditional manual deployment processes suffer from:

- Human errors during build and upload steps
- Inconsistent environments between development and production
- Slow release cycles
- Lack of automated quality checks before deployment

**Problem:** How to design an automated system that detects code changes, validates quality, builds a Docker image, and deploys a portfolio website to the cloud without manual intervention?

---

## 3. Objectives

1. Develop a responsive, professional portfolio web application
2. Implement Docker multi-stage containerization for production
3. Create a GitHub Actions workflow with CI and CD stages
4. Deploy automatically to a cloud platform (Render)
5. Document the complete system for academic evaluation

---

## 4. Literature / Background

- **Continuous Integration (CI):** Automatically integrating code changes with automated builds and tests (Fowler, 2006).
- **Continuous Deployment (CD):** Automatically releasing validated changes to production.
- **Containerization:** Docker packages applications with dependencies for portable, reproducible deployments.
- **Infrastructure as Code:** `render.yaml`, workflow YAML files define infrastructure declaratively.

---

## 5. System Design

### 5.1 Frontend Application

- **Framework:** React 19 with Vite 8
- **Styling:** Tailwind CSS 4 with custom design tokens
- **Animation:** Framer Motion for scroll and load animations
- **Sections:** Home, About, Skills, Education, Projects, Resume, Contact, Footer

### 5.2 Docker Architecture

```
node:22-alpine (builder)  →  npm ci + npm run build  →  dist/
nginx:1.27-alpine (prod)  →  serve dist/ on port 3000
```

Benefits: smaller image (~25MB nginx layer), no Node.js in production, faster startup.

### 5.3 CI/CD Workflow

| Stage | Action |
|-------|--------|
| Trigger | Push / Pull Request to main |
| Validate | npm ci, lint, test, build |
| Docker | Build image, run container, HTTP health check |
| Deploy | POST to Render deploy hook (main only) |

### 5.4 Cloud Deployment

Render hosts the Docker container as a web service with HTTPS, auto-deploy, and health monitoring.

---

## 6. Implementation

### 6.1 Portfolio Website

Component architecture with reusable `Button`, `SectionHeading`, `ProjectCard`, and section modules. Content centralized in `portfolio.js` for maintainability.

### 6.2 Testing

Vitest unit tests cover App rendering and Contact form validation/submission flows.

### 6.3 Pipeline Configuration

File: `.github/workflows/deploy.yml`  
Three jobs with dependency chain: `validate` → `docker` → `deploy`

---

## 7. Workflow Diagram

```
Developer → Git Push → GitHub
                          ↓
                    GitHub Actions
                    ├── Lint
                    ├── Test
                    ├── Build
                    ├── Docker Build
                    └── Deploy Hook → Render → Live Site
```

---

## 8. Results / Expected Outcome

- Fully functional portfolio accessible via public URL
- Automated pipeline reduces deployment time from minutes (manual) to seconds (automated trigger)
- Consistent builds via Docker eliminate "works on my machine" issues
- Academic demonstration of end-to-end DevOps competency

---

## 9. Testing

| Test Type | Tool | Status |
|-----------|------|--------|
| Unit tests | Vitest | Pass |
| Lint | ESLint | Pass |
| Build | Vite | Pass |
| Container | Docker + curl | Pass |
| CI pipeline | GitHub Actions | Pass (on push) |

---

## 10. Advantages

- **Automation:** Zero-touch deployment after initial setup
- **Quality gates:** Code cannot deploy without passing tests
- **Portability:** Docker runs identically locally and in cloud
- **Professional UI:** Industry-standard portfolio presentation
- **Extensibility:** Easy to add staging environments, Slack notifications, E2E tests

---

## 11. Limitations

- Contact form uses client-side simulation (no backend email service)
- Render free tier has cold-start latency
- Single-environment deployment (no staging branch by default)

---

## 12. Future Enhancements

- Integrate Formspree or backend API for contact form
- Add Playwright E2E tests in CI
- Push images to GitHub Container Registry
- Add monitoring (Uptime Robot, Sentry)
- Kubernetes deployment for scale demonstration

---

## 13. Conclusion

This project successfully implements a **cloud-native CI/CD pipeline** for portfolio deployment. It satisfies the academic requirement of demonstrating modern DevOps practices while delivering a production-quality user interface. The system is maintainable, documented, and ready for viva demonstration with live deployment evidence.

---

## 14. References

1. Docker Documentation — https://docs.docker.com  
2. GitHub Actions Documentation — https://docs.github.com/en/actions  
3. React Documentation — https://react.dev  
4. Render Documentation — https://render.com/docs  
5. Vite Documentation — https://vite.dev  

---

## Appendix: Viva Questions & Answers

**Q: What is CI/CD?**  
A: CI continuously integrates and validates code; CD automatically deploys validated code to production.

**Q: Why multi-stage Docker build?**  
A: To exclude build tools from the final image, reducing size and attack surface.

**Q: Why GitHub Actions?**  
A: Native integration with GitHub repos, free for public projects, YAML-based workflow definition.

**Q: Why Render over AWS?**  
A: Simpler setup for academic projects; Docker support with free tier and auto-deploy.

**Q: How does auto-deploy work?**  
A: Push to main triggers Actions; after tests pass, deploy job calls Render deploy hook; Render rebuilds Docker image and restarts service.
