from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common"


@dataclass(frozen=True)
class ReferencePeriodType:
    """
    Specifies the inclusive start and end times.

    :ivar start_time: The startTime attributes contains the inclusive
        start date for the reference period.
    :ivar end_time: The endTime attributes contains the inclusive end
        date for the reference period.
    """

    start_time: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "startTime",
            "type": "Attribute",
            "required": True,
        },
    )
    end_time: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "endTime",
            "type": "Attribute",
            "required": True,
        },
    )
