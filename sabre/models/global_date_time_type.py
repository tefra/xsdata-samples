from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.date_time_type import DateTimeType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class GlobalDateTimeType(DateTimeType):
    """
    Attributes:
        date_time: This date should be of the form YYYY-MM-DDTHH:MM:SS.
    """

    date_time: None | str = field(
        default=None,
        metadata={
            "name": "DateTime",
            "type": "Attribute",
            "required": True,
            "pattern": r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}",
        },
    )
