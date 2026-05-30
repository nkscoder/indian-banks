# Publish indian-banks to PyPI

Package: **nkscoder-indian-banks**  
PyPI account: [pypi.org/manage/account](https://pypi.org/manage/account/)

---

## 1. Create a PyPI account

1. Register at [pypi.org/account/register](https://pypi.org/account/register/)
2. Verify your email
3. Open [pypi.org/manage/account](https://pypi.org/manage/account/)

---

## 2. Create an API token (recommended)

1. Go to [pypi.org/manage/account/token](https://pypi.org/manage/account/token/)
2. Click **Add API token**
3. Scope: **Entire account** (first time) or limit to project `nkscoder-indian-banks` after first upload
4. Copy the token (`pypi-...`) — you will not see it again

Save the token locally (password manager). Do not commit it to Git.

---

## Link GitHub → PyPI (automatic publish)

PyPI does **not** have a “connect repository” button. You link them with **GitHub Actions**:

### A. Add token to GitHub (one time)

1. Open your repo: https://github.com/nkscoder/indian-banks  
2. **Settings** → **Secrets and variables** → **Actions**  
3. **New repository secret**  
   - Name: `PYPI_API_TOKEN`  
   - Value: your PyPI token (`pypi-...` from [manage account/token](https://pypi.org/manage/account/token/))  
4. Save  

### B. Push the workflow (included in this repo)

File: `.github/workflows/publish-pypi.yml`

```bash
git add .github/workflows/publish-pypi.yml pyproject.toml
git commit -m "Add GitHub Actions PyPI publish workflow"
git push origin main
```

### C. First upload OR publish via release

**Option 1 — Manual first upload** (so PyPI shows the project once):

```bash
python -m build
twine upload dist/*
```

**Option 2 — Publish from GitHub** (after secret is set):

1. On GitHub: **Releases** → **Create a new release**  
2. Tag: `v1.0.0` (must match `version` in `pyproject.toml`)  
3. Title: `v1.0.0` → **Publish release**  
4. **Actions** tab → workflow **Publish to PyPI** should run green  
5. Check https://pypi.org/project/nkscoder-indian-banks/

**Option 3 — Run workflow manually**

**Actions** → **Publish to PyPI** → **Run workflow** (uses `main` branch)

### Project URLs on PyPI

After upload, PyPI reads links from `pyproject.toml`:

- Homepage → GitHub repo  
- Documentation → README on GitHub  
- Organization → nkscoder.in  

No extra linking step on pypi.org.

---

## 3. Install build tools

```bash
cd /path/to/indian-banks
pip install --upgrade build twine
```

---

## 4. Build the package

```bash
python -m build
```

This creates:

- `dist/nkscoder_indian_banks-1.0.1.tar.gz` (source)
- `dist/nkscoder_indian_banks-1.0.1-py3-none-any.whl` (wheel)

Test the wheel locally (optional):

```bash
pip install dist/nkscoder_indian_banks-1.0.1-py3-none-any.whl
python -c "import indian_banks; print(indian_banks.__version__)"
```

---

## 5. Upload to PyPI

**TestPyPI first (recommended):**

```bash
python -m twine upload --repository testpypi dist/*

pip install --index-url https://test.pypi.org/simple/ nkscoder-indian-banks
```

**Production PyPI:**

```bash
python -m twine upload dist/*
```

When prompted:

- **Username:** `__token__`
- **Password:** your API token (`pypi-AgEIc...`)

Or use environment variables (no prompt):

```bash
export TWINE_USERNAME=__token__
export TWINE_PASSWORD=pypi-YOUR_TOKEN_HERE
python -m twine upload dist/*
```

---

## 6. Release a new version

1. Bump version in `pyproject.toml` and `indian_banks/__init__.py`
2. Rebuild and upload:

```bash
rm -rf dist/ build/ *.egg-info
python -m build
twine upload dist/*
```

3. Tag in Git:

```bash
git tag v1.0.1
git push origin v1.0.1
```

---

## Notes

- PyPI name: `nkscoder-indian-banks` (hyphen)
- Python import: `indian_banks` (underscore)
- Logos ship inside the wheel under `indian_banks/logos/`
