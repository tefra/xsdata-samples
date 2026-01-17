from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.connection_location_connection_info import (
    ConnectionLocationConnectionInfo,
)
from sabre.models.prefer_level_type import PreferLevelType
from sabre.models.request_location_type import RequestLocationType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class ConnectionType:
    """
    To specify connection locations, preference level for each, min
    connection time, and whether location is specified for stopping or
    changing.
    """

    connection_location: list[ConnectionType.ConnectionLocation] = field(
        default_factory=list,
        metadata={
            "name": "ConnectionLocation",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_occurs": 1,
            "max_occurs": 9,
        },
    )

    @dataclass
    class ConnectionLocation(RequestLocationType):
        """
        Attributes:
            inclusive:
            prefer_level:
            min_change_time: Number of minutes between connections.
            connection_info:
        """

        inclusive: bool = field(
            default=True,
            metadata={
                "name": "Inclusive",
                "type": "Attribute",
            },
        )
        prefer_level: PreferLevelType = field(
            default=PreferLevelType.PREFERRED,
            metadata={
                "name": "PreferLevel",
                "type": "Attribute",
            },
        )
        min_change_time: None | int = field(
            default=None,
            metadata={
                "name": "MinChangeTime",
                "type": "Attribute",
            },
        )
        connection_info: None | ConnectionLocationConnectionInfo = field(
            default=None,
            metadata={
                "name": "ConnectionInfo",
                "type": "Attribute",
            },
        )
