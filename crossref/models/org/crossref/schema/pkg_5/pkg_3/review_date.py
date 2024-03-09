from dataclasses import dataclass, field
from typing import Optional

from crossref.models.org.crossref.schema.pkg_5.pkg_3.day import Day
from crossref.models.org.crossref.schema.pkg_5.pkg_3.month import Month
from crossref.models.org.crossref.schema.pkg_5.pkg_3.year import Year

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class ReviewDate:
    """
    The date a review was published to a repository.
    """

    class Meta:
        name = "review_date"
        namespace = "http://www.crossref.org/schema/5.3.1"

    month: Optional[Month] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    day: Optional[Day] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    year: Optional[Year] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
