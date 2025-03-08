from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.response_location_type import ResponseLocationType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class AirportInformationType(ResponseLocationType):
    """
    Code and optional string to describe a location point.

    Attributes:
        terminal_id: Location terminal identifier.
    """

    terminal_id: None | str = field(
        default=None,
        metadata={
            "name": "TerminalID",
            "type": "Attribute",
            "pattern": r"[0-9A-Z]{1,}",
        },
    )
