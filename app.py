from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

PERSONAL = {
    "name": "KIRIJA",
    "first_name": "KIRIJA",
    "role": "B.Tech Information Technology Student | DevOps & Cloud Engineer",
    "tagline": "Building scalable cloud-native applications with automated CI/CD pipelines.",
    "email": "kirija@email.com",
    "phone": "+91 98765 43210",
    "location": "Coimbatore, Tamil Nadu, India",
    "github": "https://github.com",
    "linkedin": "https://linkedin.com",
    "twitter": "https://twitter.com",
}

NAV_LINKS = [
    {"id": "home", "label": "Home"},
    {"id": "about", "label": "About"},
    {"id": "skills", "label": "Skills"},
    {"id": "education", "label": "Education"},
    {"id": "projects", "label": "Projects"},
    {"id": "resume", "label": "Resume"},
    {"id": "contact", "label": "Contact"},
]

ABOUT = {
    "summary": (
        "Final-year Information Technology student at Kumaraguru College of Technology, "
        "Coimbatore, Tamil Nadu. Passionate about cloud infrastructure, automation, and "
        "full-stack development. I design reliable systems that ship fast — from Flask web "
        "apps to Dockerized deployments on Render with GitHub Actions."
    ),
    "highlights": [
        "3+ years building web applications",
        "CI/CD & containerization specialist",
        "Open-source contributor",
        "Agile team collaborator",
    ],
}

SKILLS = [
    {"name": "Python / Flask", "level": 90, "category": "Backend"},
    {"name": "React / Vite", "level": 88, "category": "Frontend"},
    {"name": "Docker", "level": 88, "category": "DevOps"},
    {"name": "GitHub Actions", "level": 90, "category": "DevOps"},
    {"name": "AWS / Cloud", "level": 78, "category": "Cloud"},
    {"name": "HTML / CSS / JS", "level": 94, "category": "Frontend"},
    {"name": "Node.js", "level": 82, "category": "Backend"},
    {"name": "PostgreSQL", "level": 80, "category": "Database"},
]

EDUCATION = [
    {
        "degree": "B.Tech in Information Technology",
        "institution": "Kumaraguru College of Technology, Coimbatore, Tamil Nadu",
        "period": "2022 — 2026",
        "grade": "CGPA: 8.7 / 10",
        "description": (
            "Pursuing Information Technology with focus on Cloud Computing and Software Engineering. "
            "Final-year project on automated CI/CD portfolio deployment using Flask, Docker, "
            "and GitHub Actions."
        ),
    },
    {
        "degree": "Higher Secondary (Bio Maths)",
        "institution": "SVM, Tamil Nadu",
        "period": "2020 — 2022",
        "grade": "92%",
        "description": (
            "Mathematics, Physics, Chemistry, and Biology — Bio Maths stream with strong "
            "foundation in science before entering B.Tech IT."
        ),
    },
]

PROJECTS = [
    {
        "title": "Cloud-Native CI/CD Portfolio",
        "description": (
            "Automated deployment pipeline using Flask, Docker, GitHub Actions, and Render. "
            "Multi-stage validation gates from commit to production."
        ),
        "tech": ["Flask", "Docker", "GitHub Actions", "Render"],
        "github": "https://github.com",
        "live": "#home",
        "featured": True,
    },
    {
        "title": "E-Commerce Microservices",
        "description": (
            "Distributed order processing system with API gateway, Redis caching, "
            "and Kubernetes-ready services."
        ),
        "tech": ["Node.js", "Redis", "Docker", "MongoDB"],
        "github": "https://github.com",
        "live": "#",
        "featured": True,
    },
    {
        "title": "DevOps Monitoring Dashboard",
        "description": (
            "Real-time metrics dashboard for pipeline health, build times, "
            "and deployment status across environments."
        ),
        "tech": ["Python", "Grafana", "Prometheus", "WebSockets"],
        "github": "https://github.com",
        "live": "#",
        "featured": False,
    },
    {
        "title": "Task Automation CLI",
        "description": (
            "Cross-platform CLI for scaffolding projects, running tests, "
            "and triggering deploy hooks from the terminal."
        ),
        "tech": ["Python", "Typer", "GitHub API"],
        "github": "https://github.com",
        "live": "#",
        "featured": False,
    },
]


def _skill_categories():
    seen = []
    for skill in SKILLS:
        if skill["category"] not in seen:
            seen.append(skill["category"])
    return seen


@app.route("/")
def home():
    return render_template(
        "index.html",
        personal=PERSONAL,
        nav_links=NAV_LINKS,
        about=ABOUT,
        skills=SKILLS,
        skill_categories=_skill_categories(),
        education=EDUCATION,
        projects=PROJECTS,
    )


@app.route("/resume.pdf")
def resume():
    return send_from_directory("static", "resume.pdf", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
