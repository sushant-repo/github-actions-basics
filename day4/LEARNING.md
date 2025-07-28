# Day 4 – Building Multi-Job Workflows with Dependencies and Artifact Management

---

Today was a big shift from basic CI into something that feels closer to real-world production pipelines.

---

## What I Built

I created a **staged CI workflow** with four separate jobs:

1. **Lint**

   - Runs `flake8` on my codebase
   - Fails early if style issues exist

2. **Test**

   - Uses a matrix to run tests on Python 3.8 and 3.12
   - Only runs if lint passes

3. **Build**

   - Packages my app into a `.zip` file
   - Only runs if all matrix test jobs succeed

4. **Publish**
   - Simulates a deployment step
   - Only runs on the `main` branch and if build succeeded
   - Uses `actions/download-artifact` to retrieve the `.zip`

---

## Composite Action

I created a **composite action** to avoid repeating setup logic. It:

- Sets up Python (with caching via `cache: pip`)
- Installs dependencies (if `requirements.txt` exists)

This composite action lives in:

```
.github/actions/setup-python-environment/action.yml
```

I used it in all four jobs with:

```yaml
- uses: ./.github/actions/setup-python-environment
  with:
    python-version: "3.11"
```

This worked really well for keeping things clean and DRY.

---

## Key Lessons & Concepts

### Job Isolation Is Real

Every job runs on a fresh runner — so I can’t assume anything carries over:

- No source code → I need `actions/checkout` in **every job**
- No shared Python setup → I need to set up Python in **every job**
- No shared files → I need to **upload artifacts** explicitly to pass data

### `uses:` Paths Are Relative to the Repo Root

I initially used `../actions/...`, thinking it was relative to the workflow file.  
That failed. The correct path is always:

```yaml
uses: ./.github/actions/your-action
```

No matter where the workflow lives.

### Pull Requests Don't Always See My New Action

When I opened a PR, the pipeline broke with:

```
Can't find 'action.yml'...
```

This happened because the composite action didn’t exist in `main` yet.  
PR workflows are based on `main + merge`, so the action needs to be present in `main` for PRs to use it.

**Fix:** Merge the composite action into `main` first.

---

## Bugs I Hit and Solved

| Issue                         | What Happened                    | Fix                                               |
| ----------------------------- | -------------------------------- | ------------------------------------------------- |
| `uses: ../actions/...` failed | GitHub couldn't resolve the path | Used `./.github/actions/...`                      |
| `flake8 app/` failed          | `app/` didn't exist yet          | Ensured correct directory and added `checkout@v4` |
| Composite action broke on PRs | Action didn’t exist on `main`    | Merged it first before testing PRs                |
| `pip install` failed silently | `requirements.txt` missing       | Added guard using `if [ -f requirements.txt ]`    |

---

## Technical Highlights

- Used `needs:` to control job order and dependencies
- Built test matrix for multiple Python versions
- Used `upload-artifact` and `download-artifact` to pass files between jobs
- Used `if:` conditions to make deployment job branch-specific
- Cached pip dependencies using `setup-python@v5`'s `cache: pip` feature

---

## Feeling After Day 4

I finally feel like I’m writing CI pipelines the way real teams do — with clear structure, safety nets, and logical separation of responsibilities. I also got a firsthand lesson in how GitHub Actions workflows behave differently across push vs PR vs manual triggers.

This was the first day where the setup felt like **CI engineering**, not just scripting.
