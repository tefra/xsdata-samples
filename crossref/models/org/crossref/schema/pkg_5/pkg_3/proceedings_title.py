from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class ProceedingsTitle:
    """
    The undifferentiated title of a conference proceeding.
    """

    class Meta:
        name = "proceedings_title"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "min_length": 1,
            "max_length": 511,
        },
    )
