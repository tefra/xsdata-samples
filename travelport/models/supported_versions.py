from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class SupportedVersions:
    """
    SOAP Header element that determines what version a particular request
    supports.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    ur_version: None | str = field(
        default=None,
        metadata={
            "name": "urVersion",
            "type": "Attribute",
        },
    )
    air_version: None | str = field(
        default=None,
        metadata={
            "name": "airVersion",
            "type": "Attribute",
        },
    )
    hotel_version: None | str = field(
        default=None,
        metadata={
            "name": "hotelVersion",
            "type": "Attribute",
        },
    )
    vehicle_version: None | str = field(
        default=None,
        metadata={
            "name": "vehicleVersion",
            "type": "Attribute",
        },
    )
    passive_version: None | str = field(
        default=None,
        metadata={
            "name": "passiveVersion",
            "type": "Attribute",
        },
    )
    rail_version: None | str = field(
        default=None,
        metadata={
            "name": "railVersion",
            "type": "Attribute",
        },
    )
    cruise_version: None | str = field(
        default=None,
        metadata={
            "name": "cruiseVersion",
            "type": "Attribute",
        },
    )
