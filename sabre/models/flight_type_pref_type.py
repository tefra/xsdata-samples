from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.flight_type_type import FlightTypeType
from sabre.models.prefer_level_type import PreferLevelType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class FlightTypePrefType:
    """
    Indicates preferences for certain types of flights, such as connections or
    stopovers, when used for a specific travel situation.

    Attributes:
        prefer_level:
        flight_type:
        max_connections: Indicates that if connection is chosen, then
            this attribute defines the maximum number of connections
            preferred.
    """

    prefer_level: PreferLevelType = field(
        default=PreferLevelType.PREFERRED,
        metadata={
            "name": "PreferLevel",
            "type": "Attribute",
        },
    )
    flight_type: None | FlightTypeType = field(
        default=None,
        metadata={
            "name": "FlightType",
            "type": "Attribute",
        },
    )
    max_connections: None | int | bool = field(
        default=None,
        metadata={
            "name": "MaxConnections",
            "type": "Attribute",
        },
    )
