from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class SpecialNumbering:
    """
    Issue level numbering for supplements or special issues.

    Text defining the type of special issue (e.g. "suppl") should be
    included in this element along with the number.
    """

    class Meta:
        name = "special_numbering"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "min_length": 1,
            "max_length": 15,
        },
    )
