from __future__ import annotations

from collections import Counter
from functools import lru_cache
from typing import Any, Iterable, Mapping


@lru_cache(maxsize=4096)
def normalize_label(label: str) -> str:
    """Normalize a category name once per distinct value.

    This is a frequent hot-path pattern in data processing: the same labels show up
    many times, so caching repeated normalization removes churn without changing logic.
    """
    return label.strip().lower()


def summarize_products(products: Iterable[Mapping[str, Any]]) -> dict[str, int]:
    """Aggregate product units by normalized category.

    Repeated normalization is the expensive part here, so this function keeps the
    normalization logic centralized and cache-backed.
    """
    totals: Counter[str] = Counter()

    for product in products:
        category = normalize_label(str(product.get("category", "")))
        totals[category] += int(product.get("units", 0))

    return dict(sorted(totals.items()))
