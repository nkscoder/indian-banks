# Bank data schema

Structured metadata lives in `indian_banks/data/banks.json`. Each entry describes one bank (or financial institution) with an associated logo file.

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | yes | Display name of the bank |
| `slug` | string | yes | Short unique identifier (e.g. `sbin`, `hdfc`) |
| `ifsc_prefix` | string \| null | no | First 4 characters of IFSC codes for this bank |
| `logo` | string | yes | Logo filename under `indian_banks/logos/` |
| `symbol` | string \| null | no | Symbol/icon filename (often same as `logo`) |
| `bank_type` | string \| null | no | RBI category (see below) |
| `website` | string \| null | no | Official website URL |
| `ussd` | string \| null | no | Balance enquiry USSD code (e.g. `*99#`) |

## Bank types

Values align with [RBI bank categories](https://www.rbi.org.in/scripts/banklinks.aspx):

| Value | Description |
|-------|-------------|
| `public_sector` | Public sector banks |
| `private_sector` | Private sector banks |
| `small_finance` | Small finance banks |
| `payments` | Payments banks |
| `foreign` | Foreign banks operating in India |
| `cooperative` | Cooperative / urban cooperative banks |
| `regional_rural` | Regional rural banks |
| `development` | Development financial institutions |

## Logo files

Logos are stored in `indian_banks/logos/` as PNG, JPEG, AVIF, or SVG-derived PNG files. Filenames are human-readable bank names or 4-letter codes where applicable.

## Contributing data

1. Add the logo to `indian_banks/logos/`
2. Add or update the matching object in `banks.json`
3. Keep `slug` unique across the dataset
4. Verify IFSC prefix against official RBI / bank sources when possible

## Python access

```python
from indian_banks import get_all_banks, get_bank_by_ifsc, get_logo_path

bank = get_bank_by_ifsc("SBIN0001234")
path = get_logo_path(bank)
data = bank.to_dict()
```

See [README.md](../README.md) for full usage examples.
