from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Year:
    """
    Year of publication.
    """
    class Meta:
        name = "year"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": 1400,
            "max_inclusive": 2200,
            "total_digits": 4,
        }
    )
