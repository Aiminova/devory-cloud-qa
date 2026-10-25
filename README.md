# Devory Cloud QA Test Project

![CI](https://github.com/Aiminova/devory-cloud-qa/actions/workflows/ci.yml/badge.svg)

A risk-based, end-to-end QA study of [devorycloud.com](https://devorycloud.com), a SaaS platform that deploys GitHub projects. I wrote the test plan, the automation, the manual test cases, a findings report and the CI pipeline.

## What I Built
| Layer | Content |
|---|---|
| **Automation (100+ test cases)** | Home page content, pricing and limit accuracy, SEO, login/signup, unauthorized access, broken links, consistency, responsive, accessibility, passive security, lightweight performance |
| **Manual test cases (22)** | Project/slug/limit rules, deploy states, ZIP upload, GitHub OAuth, inactivity lifecycle, billing, access isolation |
| **Findings (7)** | Repeated page titles, a "coming soon" feature button, quota design, documentation gaps |
| **Architecture** | Page Object Model, accessible locators (role/label), markers, HTML report, GitHub Actions |

## Why This Scope
The real value of the platform sits behind login (projects, deployments, quotas). So I:
1. Automated the **public surface**, which is safe and repeatable.
2. Designed the **login-protected business rules** as manual cases in `docs/test_cases.md` (3 projects, 5 updates, 500 MB, the day 15/25/30 policy).
3. Added optional authenticated tests (`tests/test_authenticated.py`) that run with my own test account via `.env`.

## Setup and Run
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium

pytest                         # all tests
pytest -m smoke                # critical fast tests
pytest -m security             # passive security + access control
pytest -m "a11y or responsive" # accessibility and responsive
pytest --headed                # run with a visible browser
```
Report: `reports/report.html` · For the optional authenticated tests, copy `.env.example` to `.env`.

## Project Structure
```
├── pages/auth_pages.py          # Login/Signup page objects
├── tests/                       # 8 test files, split by topic
├── docs/test_plan.md            # Scope, risk analysis, rules
├── docs/test_cases.md           # 26 automated + 22 manual cases
├── docs/findings.md             # Findings and bug report template
├── conftest.py                  # Shared settings
└── .github/workflows/ci.yml     # CI (push, PR, weekly)
```

## Design Decisions
- **Passive and safe:** no account creation, no deployments, no load or brute force.
- **Warnings vs. failures:** finding-style checks (security headers, console errors) do not fail the build; they show up as warnings in the report.
- **Known-issue tracking:** F-01 is tracked with `xfail`, so the test flips to XPASS once it is fixed.
- **Resilient locators:** roles and labels instead of CSS, so UI changes do not break the tests.
- **Business-rule consistency:** the same limits are compared between the home page and the docs.

## Responsible Use
These tests are low-volume and read-only. Run them only with the owner's permission or on your own systems.

---
Author: [Aiminova](https://github.com/Aiminova)
