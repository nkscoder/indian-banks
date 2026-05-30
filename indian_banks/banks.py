"""Load bank metadata and resolve logo paths."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from functools import lru_cache
from importlib import resources
from pathlib import Path
from typing import Any


@dataclass(frozen=True, slots=True)
class Bank:
    name: str
    slug: str
    ifsc_prefix: str | None
    logo: str
    symbol: str | None
    bank_type: str | None
    website: str | None
    ussd: str | None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Bank:
        return cls(
            name=data["name"],
            slug=data["slug"],
            ifsc_prefix=data.get("ifsc_prefix"),
            logo=data["logo"],
            symbol=data.get("symbol"),
            bank_type=data.get("bank_type"),
            website=data.get("website"),
            ussd=data.get("ussd"),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "slug": self.slug,
            "ifsc_prefix": self.ifsc_prefix,
            "logo": self.logo,
            "symbol": self.symbol,
            "bank_type": self.bank_type,
            "website": self.website,
            "ussd": self.ussd,
        }


def logos_dir() -> Path:
    """Return the directory containing bundled bank logo files."""
    with resources.as_file(
        resources.files("indian_banks").joinpath("logos")
    ) as path:
        return Path(path)


def _data_path() -> Path:
    with resources.as_file(
        resources.files("indian_banks").joinpath("data/banks.json")
    ) as path:
        return Path(path)


@lru_cache(maxsize=1)
def _load_banks() -> tuple[Bank, ...]:
    raw = json.loads(_data_path().read_text(encoding="utf-8"))
    return tuple(Bank.from_dict(item) for item in raw)


def get_all_banks() -> list[Bank]:
    """Return all banks in the dataset."""
    return list(_load_banks())


def get_bank(name_or_slug: str) -> Bank | None:
    """Find a bank by exact name or slug (case-insensitive)."""
    key = name_or_slug.strip().lower()
    for bank in _load_banks():
        if bank.slug == key or bank.name.lower() == key:
            return bank
    return None


get_bank_by_slug = get_bank


def get_bank_by_ifsc(ifsc: str) -> Bank | None:
    """Find a bank using a full IFSC code or 4-letter prefix."""
    prefix = ifsc.strip().upper()[:4]
    if len(prefix) < 4:
        return None
    for bank in _load_banks():
        if bank.ifsc_prefix and bank.ifsc_prefix.upper() == prefix:
            return bank
    return None


def get_logo_path(bank: Bank | str) -> Path:
    """Return the filesystem path to a bank logo."""
    if isinstance(bank, str):
        resolved = get_bank(bank)
        if resolved is None:
            raise KeyError(f"Unknown bank: {bank!r}")
        bank = resolved
    path = logos_dir() / bank.logo
    if not path.is_file():
        raise FileNotFoundError(f"Logo not found for {bank.name}: {bank.logo}")
    return path


def list_logos() -> list[str]:
    """Return sorted logo filenames bundled with the package."""
    return sorted(p.name for p in logos_dir().iterdir() if p.is_file())


def slugify(name: str) -> str:
    """Convert a bank name into a URL-friendly slug."""
    slug = name.lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    return slug.strip("-")
