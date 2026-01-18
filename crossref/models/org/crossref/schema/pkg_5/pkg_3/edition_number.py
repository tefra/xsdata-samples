from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass(kw_only=True)
class EditionNumber:
    """
    The edition number of a book. edition_number should include only a
    number and not additional text such as "edition".

    For example, you should submit "3", not "third edition" or "3rd
    edition". Roman numerals are acceptable.
    """

    class Meta:
        name = "edition_number"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "min_length": 1,
            "max_length": 15,
        },
    )
