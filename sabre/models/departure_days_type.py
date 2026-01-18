from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class DepartureDaysType:
    """
    Specify which days of week to consider for departure.

    Attributes:
        value: Value format: First letter of the name of the day or '_',
            eg. 'SMT___S' means we are interested in departing at
            Saturday, Sunday, Monday or Tuesday. Even if there are
            schedules for Wednesday, Thursday or Friday, they won't be
            returned in ISell response.
    """

    value: str = field(
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
            "length": 7,
        }
    )
