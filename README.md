# indian-banks

**Open-source Indian bank logos & structured data** — IFSC prefixes, USSD balance codes, websites, and RBI bank categories for fintech apps, UPI flows, and banking integrations.

| | |
|---|---|
| **Maintainer** | [nkscoder.in](https://nkscoder.in) |
| **Package (PyPI)** | [`nkscoder-indian-banks`](https://pypi.org/project/nkscoder-indian-banks/) |
| **Python import** | `indian_banks` |
| **Version** | 1.0.0 |
| **License** | MIT |
| **Python** | 3.10+ |

[![PyPI](https://img.shields.io/pypi/v/nkscoder-indian-banks?label=PyPI)](https://pypi.org/project/nkscoder-indian-banks/)
[![Python](https://img.shields.io/pypi/pyversions/nkscoder-indian-banks)](https://pypi.org/project/nkscoder-indian-banks/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

---

## Why this project?

Finding **reliable, verified Indian bank logos and metadata** (IFSC prefix, USSD codes, official websites) is time-consuming for fintech and banking apps.

This repo is a **single source of truth** for:

- Official PNG / JPEG / AVIF bank logos (170+ files)
- Structured JSON metadata per bank
- Python API to look up banks by slug or IFSC prefix
- Ready for PyPI install in Django, Flask, FastAPI, or data pipelines

**Keywords:** Indian banks, bank logos India, IFSC bank code, RBI bank list, UPI fintech, balance check USSD, nkscoder.

---

## Install

### From PyPI

```bash
pip install nkscoder-indian-banks
```

### From source (development)

```bash
git clone https://github.com/nkscoder/indian-banks.git
cd indian-banks
pip install -e .
```

---

## Quick start (Python)

```python
import indian_banks

# List all banks
banks = indian_banks.get_all_banks()
print(len(banks), "banks loaded")

# Lookup by IFSC code or prefix
sbi = indian_banks.get_bank_by_ifsc("SBIN0001234")
print(sbi.name, sbi.website, sbi.ussd)

# Lookup by slug
hdfc = indian_banks.get_bank("hdfc")

# Resolve logo path on disk
logo_path = indian_banks.get_logo_path(sbi)
print(logo_path)  # .../indian_banks/logos/State Bank of India.png
```

---

## Data schema

Each bank entry in `indian_banks/data/banks.json` includes:

| Field | Example | Description |
|-------|---------|-------------|
| `name` | State Bank of India | Display name |
| `slug` | `sbin` | Unique short id |
| `ifsc_prefix` | `SBIN` | First 4 chars of IFSC |
| `logo` | `State Bank of India.png` | Logo filename |
| `bank_type` | `public_sector` | RBI category |
| `website` | `https://sbi.co.in` | Official site |
| `ussd` | `*999#` | Balance enquiry code |

Full schema: **[docs/DATA.md](docs/DATA.md)**

---

## Bank slugs & logos (sample)

| Bank Name | Slug | IFSC | Logo |
| --------- | ---- | ---- | ---- |
| State Bank of India | `sbin` | SBIN | <img src="./indian_banks/logos/State Bank of India.png" height="48" alt="State Bank of India logo" /> |
| HDFC Bank | `hdfc` | HDFC | <img src="./indian_banks/logos/HDFC Bank.png" height="48" alt="HDFC Bank logo" /> |
| ICICI Bank | `icic` | ICIC | <img src="./indian_banks/logos/ICICI Bank.png" height="48" alt="ICICI Bank logo" /> |
| Punjab National Bank | `punb` | PUNB | <img src="./indian_banks/logos/Punjab National Bank.png" height="48" alt="PNB logo" /> |
| Union Bank of India | `ubin` | UBIN | <img src="./indian_banks/logos/Union Bank.png" height="48" alt="Union Bank logo" /> |

➡️ **170+ banks** with logos in `indian_banks/logos/`. Metadata enrichment is ongoing — contributions welcome.

---

## Project layout

```
indian-banks/
├── indian_banks/           # Python package
│   ├── __init__.py
│   ├── banks.py            # lookup API
│   ├── data/banks.json     # structured metadata
│   └── logos/              # bank logo files
├── docs/DATA.md            # schema documentation
├── pyproject.toml
├── PUBLISHING.md           # PyPI upload guide
├── LICENSE
└── README.md
```

---

## Publish to PyPI

To upload this package to [PyPI](https://pypi.org/):

1. Create an API token at [pypi.org/manage/account/token](https://pypi.org/manage/account/token/)
2. Build and upload — full steps in **[PUBLISHING.md](PUBLISHING.md)**

```bash
pip install build twine
python -m build
twine upload dist/*
# Username: __token__
# Password: <your-pypi-api-token>
```

GitHub Actions workflow (`.github/workflows/publish-pypi.yml`) publishes automatically on release when `PYPI_API_TOKEN` is set.

---

## Roadmap

- [x] Bank logo collection (170+ files)
- [x] JSON metadata + Python API
- [x] PyPI package (`nkscoder-indian-banks`)
- [ ] Vector (SVG) logos for all major banks
- [ ] Complete IFSC / USSD / website for every RBI-listed bank
- [ ] Automated verification against official RBI sources

Bank types reference: [RBI Official List](https://www.rbi.org.in/scripts/banklinks.aspx)

---

## Contributing

1. Fork the repo
2. Add or update a logo in `indian_banks/logos/`
3. Update `indian_banks/data/banks.json` (see [docs/DATA.md](docs/DATA.md))
4. Open a pull request

---

## About nkscoder.in

This package is maintained by **[nkscoder.in](https://nkscoder.in)** as open infrastructure for Indian banking data — logos, IFSC prefixes, and metadata for apps and fintech products.

For support or custom integrations, visit [https://nkscoder.in](https://nkscoder.in).

---

## License

Copyright © 2026 [nkscoder.in](https://nkscoder.in).

Released under the [MIT License](LICENSE). Logos remain property of their respective banks; use only for identification and reference in applications.
