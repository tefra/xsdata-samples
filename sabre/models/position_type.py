from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class PositionType:
    """
    Used to identify geospatial postion of the requesting entity.
    """

    latitude: None | str = field(
        default=None,
        metadata={
            "name": "Latitude",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        },
    )
    longitude: None | str = field(
        default=None,
        metadata={
            "name": "Longitude",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        },
    )
    altitude: None | str = field(
        default=None,
        metadata={
            "name": "Altitude",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        },
    )
