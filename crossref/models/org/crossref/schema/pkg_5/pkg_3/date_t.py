from dataclasses import dataclass, field
from typing import Optional

from crossref.models.org.crossref.schema.pkg_5.pkg_3.date_t_media_type import (
    DateTMediaType,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.day import Day
from crossref.models.org.crossref.schema.pkg_5.pkg_3.month import Month
from crossref.models.org.crossref.schema.pkg_5.pkg_3.year import Year

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class DateT:
    class Meta:
        name = "date_t"

    month: Optional[Month] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
        },
    )
    day: Optional[Day] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
        },
    )
    year: Optional[Year] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
            "required": True,
        },
    )
    media_type: DateTMediaType = field(
        default=DateTMediaType.PRINT,
        metadata={
            "type": "Attribute",
        },
    )
