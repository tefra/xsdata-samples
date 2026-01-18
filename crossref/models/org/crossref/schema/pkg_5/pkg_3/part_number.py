from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class PartNumber:
    """
    The part number of a given volume.

    In some cases, a book set will have multiple parts, and then one or
    more volumes within each part. The part number of a given volume should
    be deposited in this element.
    """

    class Meta:
        name = "part_number"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "min_length": 1,
            "max_length": 15,
        },
    )
