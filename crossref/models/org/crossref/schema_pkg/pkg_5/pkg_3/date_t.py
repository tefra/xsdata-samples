from dataclasses import dataclass, field
from typing import Optional
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.date_t_media_type import DateTMediaType

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class DateT:
    class Meta:
        name = "date_t"

    month: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
            "min_inclusive": 1,
            "max_inclusive": 34,
            "total_digits": 2,
        }
    )
    day: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
            "min_inclusive": 1,
            "max_inclusive": 31,
            "total_digits": 2,
        }
    )
    year: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
            "required": True,
            "min_inclusive": 1400,
            "max_inclusive": 2200,
            "total_digits": 4,
        }
    )
    media_type: DateTMediaType = field(
        default=DateTMediaType.PRINT,
        metadata={
            "type": "Attribute",
        }
    )
