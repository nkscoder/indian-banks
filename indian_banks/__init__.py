"""Indian Banks — logos and structured metadata for RBI-recognized banks.

Author: Nitesh Kumar Singh — https://github.com/nkscoder
"""

__version__ = "1.0.1"
__author__ = "Nitesh Kumar Singh"

from indian_banks.banks import (
    Bank,
    get_all_banks,
    get_bank,
    get_bank_by_ifsc,
    get_bank_by_slug,
    get_logo_path,
    list_logos,
    logos_dir,
)

__all__ = [
    "Bank",
    "__version__",
    "get_all_banks",
    "get_bank",
    "get_bank_by_ifsc",
    "get_bank_by_slug",
    "get_logo_path",
    "list_logos",
    "logos_dir",
]
