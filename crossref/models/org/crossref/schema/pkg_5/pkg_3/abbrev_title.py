from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass(kw_only=True)
class AbbrevTitle:
    """
    Common abbreviation or abbreviations used when citing a journal.

    It is recommended that periods be included after abbreviated words
    within the title.
    """

    class Meta:
        name = "abbrev_title"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "min_length": 1,
            "max_length": 150,
        },
    )
