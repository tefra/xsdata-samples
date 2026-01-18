from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.prefer_level_type import PreferLevelType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class BookingClassPrefType:
    """
    Booking class code and preference level for specifying booking classes
    preferred/not preferred in a request.

    Attributes:
        res_book_desig_code: Booking class code
        prefer_level:
    """

    res_book_desig_code: str = field(
        metadata={
            "name": "ResBookDesigCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Z]{1,2}",
        }
    )
    prefer_level: PreferLevelType = field(
        default=PreferLevelType.PREFERRED,
        metadata={
            "name": "PreferLevel",
            "type": "Attribute",
        },
    )
