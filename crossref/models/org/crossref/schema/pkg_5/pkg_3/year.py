from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass(kw_only=True)
class Year:
    """
    Year of publication.
    """

    class Meta:
        name = "year"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: int = field(
        metadata={
            "required": True,
            "min_inclusive": 1400,
            "max_inclusive": 2200,
            "total_digits": 4,
        }
    )
