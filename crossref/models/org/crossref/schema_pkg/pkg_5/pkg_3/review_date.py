from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class ReviewDate:
    """
    The date a review was published to a repository.
    """
    class Meta:
        name = "review_date"
        namespace = "http://www.crossref.org/schema/5.3.1"

    month: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 34,
            "total_digits": 2,
        }
    )
    day: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 31,
            "total_digits": 2,
        }
    )
    year: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_inclusive": 1400,
            "max_inclusive": 2200,
            "total_digits": 4,
        }
    )
