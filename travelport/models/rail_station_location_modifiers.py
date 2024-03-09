from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.rail_location_1 import RailLocation1

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class RailStationLocationModifiers:
    """
    Request object used to request specific rail station locations.

    Parameters
    ----------
    rail_location
    country_code
        2 character country code such as FR.
    distributor
        2 character Rail distributor code such as TL or 2C.
    description
        A city name or station name such as Paris or Paris Nord.
    active
        The value “false” will return stations that are no longer active but
        remain on the table because existing bookings may reference them.
        The default is “true” which returns only active locations.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    rail_location: None | RailLocation1 = field(
        default=None,
        metadata={
            "name": "RailLocation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    country_code: None | str = field(
        default=None,
        metadata={
            "name": "CountryCode",
            "type": "Attribute",
            "length": 2,
        },
    )
    distributor: None | str = field(
        default=None,
        metadata={
            "name": "Distributor",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        },
    )
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
        },
    )
    active: bool = field(
        default=True,
        metadata={
            "name": "Active",
            "type": "Attribute",
        },
    )
