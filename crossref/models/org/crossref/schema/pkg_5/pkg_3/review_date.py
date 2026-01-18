from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.org.crossref.schema.pkg_5.pkg_3.day import Day
from crossref.models.org.crossref.schema.pkg_5.pkg_3.month import Month
from crossref.models.org.crossref.schema.pkg_5.pkg_3.year import Year

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass(kw_only=True)
class ReviewDate:
    """
    The date a review was published to a repository.
    """

    class Meta:
        name = "review_date"
        namespace = "http://www.crossref.org/schema/5.3.1"

    month: Month = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    day: Day = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    year: Year = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
