# DevOps Assessment Checklist - Ipswich Retail E-commerce Project

## Overview
- **Deadline:** September 19, 2025 (12:00 noon)
- **Report:** 3000 words (+10% allowed)
- **Weight:** 60% of module grade
- **Deployment:** Railway.com (free tier)

---

## 1. APPLICATION DEVELOPMENT (20%)

| Task | Status | Details | Notes |
|------|--------|---------|-------|
| Django project setup | [ ] | Initialize Django project with MVT architecture | |
| Product model creation | [ ] | Create models for products, categories, orders | |
| Home page (View + Template) | [ ] | Display product catalog | Page 1/4 |
| Product detail page | [ ] | Individual product view | Page 2/4 |
| Shopping cart page | [ ] | Add to cart functionality | Page 3/4 |
| Checkout/Order page | [ ] | Order processing | Page 4/4 |
| Admin panel configuration | [ ] | Configure Django admin (not counted in 4 pages) | |
| Basic authentication | [ ] | User login/registration | |
| Database setup | [ ] | PostgreSQL configuration for Railway | |
| Static files configuration | [ ] | CSS/JS serving | |
| Simple UI design | [ ] | Bootstrap/Tailwind for clean, simple interface | Use CodePen templates |

---

## 2. DEVOPS IMPLEMENTATION (20%)

### 2.1 Planning Phase
| Task | Status | Details | Notes |
|------|--------|---------|-------|
| Frontend mockup/wireframe | [ ] | Create wireframes for 4 pages | Use Draw.io/Lucidchart |
| Backend architecture diagram | [ ] | Django MVT architecture diagram | |
| Team composition plan | [ ] | Define dev/ops roles (theoretical) | |
| DevOps pipeline diagram | [ ] | Full CI/CD workflow visualization | |

### 2.2 Version Control
| Task | Status | Details | Notes |
|------|--------|---------|-------|
| GitHub repository setup | [ ] | Public repository | Must be public |
| Branching strategy | [ ] | main/develop/feature branches | Document strategy |
| Git workflow documentation | [ ] | How branches are used | |
| .gitignore configuration | [ ] | Exclude secrets, env files | |

### 2.3 Containerization
| Task | Status | Details | Notes |
|------|--------|---------|-------|
| Dockerfile creation | [ ] | Multi-stage Docker build | |
| docker-compose.yml | [ ] | Local development setup | |
| Container testing locally | [ ] | Verify containers work | Take screenshots |
| Environment variables setup | [ ] | .env file configuration | |

### 2.4 CI/CD Pipeline
| Task | Status | Details | Notes |
|------|--------|---------|-------|
| GitHub Actions workflow | [ ] | .github/workflows/main.yml | Or Jenkins/GitLab CI |
| Automated build on push | [ ] | Trigger on main branch | |
| Automated testing in pipeline | [ ] | Run tests before deploy | |
| Automated deployment | [ ] | Deploy to Railway on success | |
| Pipeline success notification | [ ] | Optional: Slack integration | |

### 2.5 Automated Testing
| Task | Status | Details | Notes |
|------|--------|---------|-------|
| Unit tests for models | [ ] | Test product, order models | |
| Unit tests for views | [ ] | Test view logic | |
| Integration tests | [ ] | Test full workflows | |
| End-to-end tests | [ ] | Optional: Selenium/Playwright | |
| Test coverage report | [ ] | Generate coverage metrics | |

### 2.6 Continuous Delivery
| Task | Status | Details | Notes |
|------|--------|---------|-------|
| Railway deployment setup | [ ] | Connect GitHub to Railway | |
| Production environment config | [ ] | Environment variables on Railway | |
| Database migration automation | [ ] | Auto-run migrations on deploy | |
| Zero-downtime deployment | [ ] | Rolling updates configuration | |

### 2.7 Monitoring & Logging
| Task | Status | Details | Notes |
|------|--------|---------|-------|
| Application logging | [ ] | Django logging configuration | |
| Error tracking | [ ] | GitHub Issues or basic error logs | |
| Deployment notifications | [ ] | Slack/Teams integration (optional) | |
| Uptime monitoring | [ ] | Simple health check endpoint | |
| Resource usage tracking | [ ] | Railway dashboard monitoring | |

---

## 3. DOCUMENTATION & SCREENSHOTS (6%)

| Task | Status | Details | Notes |
|------|--------|---------|-------|
| Planning phase screenshots | [ ] | Wireframes, architecture diagrams | Label clearly |
| Git workflow screenshots | [ ] | Branch strategy, commits, PRs | |
| Dockerfile screenshots | [ ] | Show Docker configuration | |
| CI/CD pipeline screenshots | [ ] | GitHub Actions runs, success/failures | |
| Test execution screenshots | [ ] | Test results, coverage reports | |
| Deployment screenshots | [ ] | Railway dashboard, deployment logs | |
| Live application screenshots | [ ] | All 4 pages functioning | |
| Monitoring screenshots | [ ] | Logs, error tracking | |
| README.md file | [ ] | Project setup instructions | In GitHub repo |

---

## 3.1 REPORT IMAGES & SCREENSHOTS TRACKER

### Images needed for report with captions:

| # | Image Type | Caption | Status | Location |
|---|------------|---------|--------|----------|
| 1 | Architecture Diagram | Figure 1: Django MVT Architecture for Ipswich Retail E-commerce System | [ ] | planning/architecture.md |
| 2 | DevOps Pipeline Diagram | Figure 2: Complete DevOps CI/CD Pipeline Workflow | [ ] | Create diagram |
| 3 | Wireframe - Home Page | Figure 3: Home Page Wireframe - Product Catalog View | [ ] | planning/wireframes.md |
| 4 | Wireframe - Product Detail | Figure 4: Product Detail Page Wireframe | [ ] | planning/wireframes.md |
| 5 | Wireframe - Cart | Figure 5: Shopping Cart Page Wireframe | [ ] | planning/wireframes.md |
| 6 | Wireframe - Checkout | Figure 6: Checkout and Order Confirmation Wireframe | [ ] | planning/wireframes.md |
| 7 | GitHub Repository | Figure 7: GitHub Repository Structure and File Organization | [ ] | screenshots/ |
| 8 | Git Commit History | Figure 8: Git Commit History Showing Incremental Development | [ ] | screenshots/ |
| 9 | Dockerfile Configuration | Figure 9: Dockerfile for Containerization | [ ] | screenshots/ |
| 10 | docker-compose.yml | Figure 10: Docker Compose Multi-Container Configuration | [ ] | screenshots/ |
| 11 | Test Execution | Figure 11: Automated Test Suite Execution Results | [ ] | screenshots/ |
| 12 | Test Coverage Report | Figure 12: Code Coverage Report (>80% target) | [ ] | screenshots/ |
| 13 | GitHub Actions Workflow | Figure 13: GitHub Actions CI/CD Pipeline Configuration | [ ] | screenshots/ |
| 14 | CI/CD Pipeline Run | Figure 14: Successful GitHub Actions Pipeline Execution | [ ] | screenshots/ |
| 15 | Railway Dashboard | Figure 15: Railway Deployment Dashboard | [ ] | screenshots/ |
| 16 | Railway Deployment Logs | Figure 16: Railway Deployment Logs and Status | [ ] | screenshots/ |
| 17 | Home Page Live | Figure 17: Live Application - Home Page with Product Catalog | [ ] | screenshots/ |
| 18 | Product Detail Live | Figure 18: Live Application - Product Detail Page | [ ] | screenshots/ |
| 19 | Shopping Cart Live | Figure 19: Live Application - Shopping Cart Functionality | [ ] | screenshots/ |
| 20 | Checkout Page Live | Figure 20: Live Application - Checkout Process | [ ] | screenshots/ |
| 21 | Django Admin | Figure 21: Django Admin Panel for Product Management | [ ] | screenshots/ |
| 22 | Application Logs | Figure 22: Application Logging and Monitoring | [ ] | screenshots/ |
| 23 | Database Models | Figure 23: Django Models - Database Schema | [ ] | screenshots/ |

### Word Count Tracking

| Section | Target Words | Actual Words | Status |
|---------|--------------|--------------|--------|
| Title Page | - | - | [ ] |
| Introduction | 300 | 0 | [ ] |
| DevOps Workflow | 600 | 0 | [ ] |
| Planning Phase | 200 | 0 | [ ] |
| Code Phase | 200 | 0 | [ ] |
| Build Phase | 200 | 0 | [ ] |
| Test Phase | 200 | 0 | [ ] |
| Deploy Phase | 200 | 0 | [ ] |
| Monitor Phase | 200 | 0 | [ ] |
| Benefits & Limitations | 600 | 0 | [ ] |
| Lessons Learned | 600 | 0 | [ ] |
| Challenges Faced | 200 | 0 | [ ] |
| Alternative Tools | 200 | 0 | [ ] |
| Future of DevOps | 200 | 0 | [ ] |
| Conclusion | 120 | 0 | [ ] |
| **TOTAL** | **~3000** | **0** | **[ ]** |

**Note:** Use `wc -w filename.md` command to validate word count before submission.

---

## 4. REPORT WRITING (3000 words)

### 4.1 Title Page
| Task | Status | Details | Notes |
|------|--------|---------|-------|
| Create title page | [ ] | Include S number (NOT your name) | |

### 4.2 Introduction (10%)
| Task | Status | Details | Notes |
|------|--------|---------|-------|
| Describe current system flaws | [ ] | Monolithic issues at Ipswich Retail | |
| Justify DevOps adoption | [ ] | Breaking dev/ops silos | |
| Explain solution approach | [ ] | Django MVT + DevOps principles | |
| Cover all DevOps principles | [ ] | CI/CD, version control, automation, monitoring, security, collaboration | |

### 4.3 DevOps Workflow (20%)
| Task | Status | Details | Notes |
|------|--------|---------|-------|
| Plan phase explanation | [ ] | Wireframes, architecture, team | |
| Code phase explanation | [ ] | Django development, Git workflow | |
| Build phase explanation | [ ] | Docker containerization | |
| Test phase explanation | [ ] | Automated testing strategy | |
| Delivery phase explanation | [ ] | CI/CD pipeline details | |
| Deploy phase explanation | [ ] | Railway deployment process | |
| Communication phase | [ ] | Slack/Teams/GitHub Issues | |
| Monitor phase explanation | [ ] | Logging, monitoring tools | |
| Include key screenshots | [ ] | Properly labeled with captions | |
| Include diagrams | [ ] | DevOps pipeline, architecture | |
| Tools justification | [ ] | Why each tool was chosen | |
| Experience/reflections | [ ] | What went well, what went wrong | |

### 4.4 Benefits & Limitations Analysis (20%)
| Task | Status | Details | Notes |
|------|--------|---------|-------|
| Benefits of created pipeline | [ ] | Speed, reliability, collaboration | |
| Limitations of approach | [ ] | Honest assessment | |
| Open-source tools pros | [ ] | Cost, flexibility, community | |
| Open-source tools cons | [ ] | Support, scalability, features | |
| Balanced perspective | [ ] | Not skewed to one side | |

### 4.5 Lessons Learned & Future (20%)
| Task | Status | Details | Notes |
|------|--------|---------|-------|
| Implementation challenges | [ ] | Specific problems faced | |
| Lessons learned | [ ] | What was learned from PoC | |
| Alternative tools discussion | [ ] | Compare with other options | |
| Recommendations for scale | [ ] | Full production deployment advice | |
| Future of DevOps | [ ] | Trends, tools, practices | |

### 4.6 Conclusion (4%)
| Task | Status | Details | Notes |
|------|--------|---------|-------|
| Summary of implementation | [ ] | Brief recap | |
| Key insights | [ ] | Main takeaways | |
| Reflection on practice | [ ] | Personal experience | |
| Original thoughts | [ ] | Demonstrate understanding | |

### 4.7 References
| Task | Status | Details | Notes |
|------|--------|---------|-------|
| Harvard referencing style | [ ] | University of Suffolk format | |
| Cite all sources | [ ] | Academic papers, documentation | |
| No plagiarism | [ ] | Original work only | |

---

## 5. SUBMISSION REQUIREMENTS

| Task | Status | Details | Notes |
|------|--------|---------|-------|
| Word count check | [ ] | 3000 words (+10% max) | Excludes tables, diagrams, references |
| File naming | [ ] | sXXXXXX-DevOps_II.pdf | Use your S number |
| GitHub link in report | [ ] | Public repository URL | |
| Live app link in report | [ ] | Railway deployment URL | |
| Username/password included | [ ] | Login credentials for app | |
| GitHub repo is public | [ ] | Must be accessible | |
| GitHub repo is functional | [ ] | Code runs successfully | |
| Report tone | [ ] | Professional, for CEO/manager | Not too technical |
| Proofread report | [ ] | Grammar, spelling, clarity | |
| Submit to Brightspace | [ ] | Before deadline | |

---

## 6. GRADING OPTIMIZATION CHECKLIST

### To Achieve First Class (70-100%)
| Criterion | Target | Status |
|-----------|--------|--------|
| Introduction depth | Clear outline of flaws + comprehensive DevOps solution | [ ] |
| MVT functionality | Fully functional, efficient, good error handling | [ ] |
| DevOps integration | All 8 phases well-defined and automated | [ ] |
| Benefits/limitations balance | Nuanced, exceptional understanding | [ ] |
| Lessons learned | Exceptional insights, clear future directions | [ ] |
| Presentation quality | High-quality visuals, clear organization | [ ] |
| Conclusion | Very clear, impressive insights, original | [ ] |

---

## 7. RECOMMENDED TECH STACK (Simple & Effective)

| Component | Technology | Reason |
|-----------|-----------|--------|
| **Backend** | Django 4.x | Required by assessment |
| **Frontend** | Bootstrap 5 | Simple, clean, no complex JS needed |
| **Database** | PostgreSQL | Railway native support |
| **Containerization** | Docker + docker-compose | Standard, required |
| **CI/CD** | GitHub Actions | Free, simple, integrated with GitHub |
| **Version Control** | Git + GitHub | Free, standard |
| **Deployment** | Railway.com | Free tier, easy deployment, PostgreSQL included |
| **Testing** | Django TestCase + Coverage.py | Built-in, simple |
| **Monitoring** | Django logging + Railway logs | Free, sufficient for PoC |
| **Communication** | GitHub Issues (optional: Slack) | Free, simple tracking |

---

## 8. IMPLEMENTATION TIMELINE

| Phase | Tasks | Priority |
|-------|-------|----------|
| **Week 1** | Planning, wireframes, architecture diagrams, GitHub setup | HIGH |
| **Week 2** | Django app development (4 pages), models, views, templates | HIGH |
| **Week 3** | Docker setup, testing implementation, CI/CD pipeline | HIGH |
| **Week 4** | Railway deployment, monitoring, final testing | HIGH |
| **Week 5** | Report writing (intro, DevOps workflow) | HIGH |
| **Week 6** | Report writing (benefits/limitations, lessons, conclusion) | HIGH |
| **Week 7** | Review, screenshots, proofreading, submission | HIGH |

---

## PROGRESS TRACKER

- [ ] **Phase 1: Planning Complete** (Diagrams, wireframes, architecture)
- [ ] **Phase 2: Development Complete** (Django app working locally)
- [ ] **Phase 3: DevOps Setup Complete** (Docker, CI/CD, tests)
- [ ] **Phase 4: Deployment Complete** (Live on Railway)
- [ ] **Phase 5: Documentation Complete** (Screenshots, notes)
- [ ] **Phase 6: Report Complete** (3000 words)
- [ ] **Phase 7: Submission Complete** (Submitted to Brightspace)

---

## NOTES

### Key Points to Remember:
1. Focus on **simplicity** - assessment completion over complexity
2. Take **screenshots at every step** - critical for report
3. Document **your experience** - reflections are important
4. **Test everything** - automation must work
5. Keep UI **simple** - use Bootstrap templates
6. **No paid services** - only free tier tools
7. Keep repository **public and functional**
8. Report tone: **professional but accessible** (for CEO/manager)
9. **No ChatGPT** - original work only
10. **Harvard referencing** - cite all sources

### Common Pitfalls to Avoid:
- Over-engineering the application
- Missing screenshots
- Not documenting reflections/challenges
- Exceeding word count by >10%
- Using paid services
- Making repository private
- Not including live link/GitHub link
- Poor referencing
- Skipping tests
- No monitoring/logging

---

**Last Updated:** [DATE]
**Status:** [IN PROGRESS / COMPLETED]
