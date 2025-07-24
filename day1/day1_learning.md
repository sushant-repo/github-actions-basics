# Day 1 Journal — Getting Started with Git, GitHub & CI/CD

---

## Understanding Git

Git is a **local version control system** that keeps track of code changes on your computer. To use Git, you need to ensure it is installed.

### Check Git Installation

```bash
git --version
```

If Git is not installed, download it from:  
🔗 https://git-scm.com/downloads

### Setting Up a Git Project

1. Create a new folder and open it in your editor (e.g., VS Code).
2. Open a terminal (in VS Code: `Terminal > New Terminal`).
3. Navigate to the project folder (if not already there).
4. Run:

```bash
git init
```

This initializes Git and creates a hidden `.git` folder that enables Git tracking.

---

### Common Git Commands

| Command                      | Purpose                                        |
| ---------------------------- | ---------------------------------------------- |
| `git status`                 | Check current changes                          |
| `git add .`                  | Stage all changes                              |
| `git add <file>`             | Stage specific file(s)                         |
| `git commit -m "message"`    | Commit staged changes                          |
| `git commit -am "message"`   | Add & commit modified files in one step        |
| `git push origin main`       | Push commits to the main branch on GitHub      |
| `git push -u origin main`    | Set the upstream and push to main (first push) |
| `git log`                    | View history of commits                        |
| `git reset HEAD~1`           | Uncommit the last commit (keep changes)        |
| `git reset HEAD <commit-id>` | Reset to a specific commit (soft reset)        |
| `git reset --soft HEAD~1`    | Undo commit, keep changes staged               |
| `git reset --hard HEAD~1`    | Undo commit and discard all changes            |

---

### Connecting to GitHub

Even though commits are saved locally, **they’re not backed up** unless you push them to a remote platform like GitHub.

1. Create a repository on GitHub.
2. Link it with your local Git project:

```bash
git remote add origin <repo-url>
```

3. Push changes to GitHub:

```bash
git push origin main
```

---

## What I Understood About CI/CD

### Continuous Integration (CI)

- CI ensures that **code from multiple developers integrates cleanly**.
- Developers work on **short-lived feature branches** instead of pushing directly to `main`.
- Pull Requests are used for **code review**.
- CI workflows automate the process of **building, testing, and linting** to prevent broken code from being merged.

**Why this matters:**  
Even peer-reviewed code can break things if not tested properly — CI catches those cases before merge.

### Continuous Delivery (CD)

- CD automates the delivery of code to its target environment:
  - Testing
  - Staging
  - Production
- The goal is to **reduce manual deployment steps** and deliver faster and safer.

---

## My First GitHub Actions Workflows

- Workflows must be defined in:

```
.github/workflows/
```

- I wrote two workflows:

### 1. `hello.yml`

- Triggered on push to `main`
- Runs a Python script: `hello.py`
- Taught me about triggers, jobs, steps, and runners

### 2. `system-info.yml`

- Triggered manually using `workflow_dispatch`
- Prints system info and uses environment variables
- Helped me understand:
  - Manual triggers
  - `env:` at job and step level
  - How GitHub-hosted runners behave

---

## 📁 My Learning Repo Structure

To keep things clean and organized, I followed this pattern:

```
github-actions-basics/
├── day1/
│   ├── hello.py
│   ├── test_hello.py
│   ├── DAY1_LEARNING.md
│   ├── README.md
│   └── .github/workflows/
│       ├── hello.yml
│       └── system_info.yml
├── .github/workflows/
│   └── hello.yml (active workflow for CI)
```

Each `day-X/` folder contains:

- Scripts
- Archived workflows
- Daily learning journal

---

## Use Case Solved Today

**Scenario:**  
Ensure that the `hello.py` script runs correctly on every push to `main`, to prevent runtime errors.

**Solution:**  
Created a CI workflow that:

- Runs a test script (`test_hello.py`) using `pytest`
- Uses a GitHub-hosted runner
- Fails the workflow if the output is wrong

**Value:**  
This is a real example of how CI helps developers maintain reliability during collaboration.

---

## What I Did Today

1. Created the repo: `github-actions-basics`
2. Installed Git and connected local repo to GitHub
3. Created `hello.py` and `test_hello.py` inside `day1/`
4. Wrote and tested two GitHub Actions workflows
5. Learned how CI/CD can be automated with GitHub Actions
6. Organized code per-day for clarity and growth
7. Wrote this journal to track my learning and use cases

---

## Summary

- Git tracks code changes locally
- GitHub hosts code in the cloud
- CI helps catch integration bugs before merge
- CD automates delivery to environments
- GitHub Actions enables automated CI/CD
- I solved a real use case: "automatically verify my script works on push"

I’m now ready to move to Day 2: Workflow syntax, matrix builds, and advanced triggers!
