from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Day:
    """Day of publication.

    The should must be expressed with a leading zero if it is less than
    10 (e.g. submit "05", not "5").
    """

    class Meta:
        name = "day"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 31,
            "total_digits": 2,
        },
    )
