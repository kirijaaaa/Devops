# PPT Presentation Outline (10–15 Slides)

## Slide 1: Title
- **Cloud-Native CI/CD Pipeline for Automated Portfolio Deployment**
- Your Name, Department, Guide Name, Year

## Slide 2: Problem Statement
- Manual deployment is slow and error-prone
- Need automation from code change to live website

## Slide 3: Objectives
- Portfolio website
- Docker containerization
- GitHub Actions CI/CD
- Cloud auto-deployment

## Slide 4: Technology Stack
- React, Vite, Tailwind, Framer Motion
- Docker, Nginx
- GitHub Actions, Render

## Slide 5: System Architecture
- Show diagram from ARCHITECTURE.md
- Developer → GitHub → Actions → Render

## Slide 6: Portfolio Features
- Screenshots: Home, Skills, Projects, Contact
- Responsive design highlights

## Slide 7: Docker Implementation
- Multi-stage build diagram
- Builder stage vs Production stage
- Port 3000, nginx SPA routing

## Slide 8: CI/CD Pipeline
- Workflow stages: Lint → Test → Build → Docker → Deploy
- Triggers: push, pull_request

## Slide 9: Cloud Deployment
- Render setup steps
- Deploy hook integration
- Live URL demo

## Slide 10: Demo / Live URL
- Screen recording or live site walkthrough
- Show GitHub Actions green check

## Slide 11: Testing
- Vitest unit tests
- Docker health check in CI

## Slide 12: Results
- Automated deployment achieved
- Reduced manual steps to zero

## Slide 13: Advantages & Limitations
- Pros: automation, consistency, professional UI
- Cons: free tier cold start, simulated contact form

## Slide 14: Future Work
- E2E tests, Kubernetes, monitoring

## Slide 15: Conclusion & Q&A
- Project successfully demonstrates DevOps pipeline
- Thank you

---

## Viva Demo Script (2 minutes)

1. Open local site: `npm run dev`
2. Show GitHub repo and Actions workflow file
3. Push a small change → show pipeline running
4. Open Render dashboard and live URL
5. Explain multi-stage Dockerfile in 30 seconds
