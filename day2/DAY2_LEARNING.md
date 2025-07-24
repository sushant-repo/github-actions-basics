# Day 2 Learning Journal: GitHub Actions Matrix & Advanced Workflow Concepts

## What I Learned Today

### 1. What is a Matrix in GitHub Actions?

- A **matrix** allows me to run the **same workflow logic across different input combinations**.
- GitHub automatically creates jobs for each unique combination in the matrix.
- This is especially useful for:
  - Testing across multiple Python/Node versions
  - Running the same tasks in multiple environments or regions
  - Deploying conditionally across stages (dev, staging, prod)

### 2. Matrix Combinations vs Pairing

Initially, I used:

```yaml
matrix:
  python-version: [3.9, 3.11]
  greeting: ["Hello from 3.9", "Hello from 3.11"]
```

But this resulted in 2 × 2 = 4 jobs:

| python-version | greeting        |
| -------------- | --------------- |
| 3.9            | Hello from 3.9  |
| 3.9            | Hello from 3.11 |
| 3.11           | Hello from 3.9  |
| 3.11           | Hello from 3.11 |

I learned that this is called a **cartesian product**, and GitHub doesn't know that I only want "matched" combinations.

Although I did not yet test it, I now understand that to pair values correctly, I should use an explicit pair-matrix with `include` like this:

```yaml
matrix:
  include:
    - python-version: 3.9
      greeting: "Hello from 3.9"
    - python-version: 3.11
      greeting: "Hello from 3.11"
```

This will correctly create only 2 jobs, each using the right pair.

---

### 3. Workflow Dispatch and Fail-Fast

- I added `workflow_dispatch` to allow manual runs of the workflow.
- I also experimented with `fail-fast: true` and `false`:
  - When `true`, if one job fails, others are **cancelled**
  - When `false`, all jobs run even if one fails

This is useful for controlling CI cost, time, and prioritizing error visibility.

---

### 4. Environment Variables in Workflows

I learned to set job-level `env` like this:

```yaml
env:
  GREETING: ${{ matrix.greeting }}
```

Initially I tried to access the variable with:

```bash
echo ${{ GREETING }}
```

But I learned that the correct syntax is:

```bash
echo ${{ env.GREETING }}
```

Or directly from the shell:

```bash
echo "$GREETING"
```

Inside Python, I can use:

```python
import os
os.environ.get("GREETING")
```

---

### 5. Common Gotchas I Ran Into

- ❌ **Incorrect matrix syntax** like `$(matrix.python-version)` → should be `${{ matrix.python-version }}`
- ❌ Using cartesian matrix when I wanted pairs
- ❌ Unexpected duplicate jobs — fixed by removing `push:` trigger and using only `pull_request`
- ✅ Learned how `gh pr create` works and how to trigger PRs from CLI
- ✅ Understood how GitHub expands matrix jobs at runtime

---

## 🛠️ What I Did Today

- Created `day2/` directory
- Created `test_matrix.yml` with matrix builds across Python versions
- Verified CI ran correctly per version
- Added environment variables to pass dynamic messages into jobs
- Debugged matrix misbehavior (4 jobs instead of 2)
- Learned how to fix matrix pairings using `include` (not tested yet)
- Tested fail-fast strategies
- Triggered workflows manually via dispatch
- Created PR using GitHub CLI

---

## Reflections

I now understand that a matrix in GitHub Actions is a **job generator**, and that it’s up to me to control the logic that determines how many jobs run and what each job does.

When I want logical pairs of configuration values (like version and region, or version and message), I should **use `matrix.include`**, not parallel arrays.

This understanding will help me avoid unnecessary compute usage, bloated logs, and CI confusion in real projects.
