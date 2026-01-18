from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass(kw_only=True)
class RailInfo:
    """
    Container for rail-related information required for retrieving a rail
    seat map/coach map.

    Parameters
    ----------
    origin
        The IATA location code for this origination of this entity.
    rail_loc_origin
        RCH specific origin code (a.k.a UCodes) which uniquely identifies a
        train station.
    destination
        The IATA location code for this destination of this entity.
    rail_loc_destination
        RCH specific destination code (a.k.a UCodes) which uniquely
        identifies a train station.
    departure_time
        The date and time at which this entity departs. This does not
        include time zone information since it can be derived from the
        origin location.
    arrival_time
        The date and time at which this entity arrives at the destination.
        This does not include time zone information since it can be derived
        from the origin location.
    train_number
    provider_code
    supplier_code
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    origin: None | str = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        },
    )
    rail_loc_origin: None | str = field(
        default=None,
        metadata={
            "name": "RailLocOrigin",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 8,
            "white_space": "collapse",
        },
    )
    destination: None | str = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        },
    )
    rail_loc_destination: None | str = field(
        default=None,
        metadata={
            "name": "RailLocDestination",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 8,
            "white_space": "collapse",
        },
    )
    departure_time: str = field(
        metadata={
            "name": "DepartureTime",
            "type": "Attribute",
            "required": True,
        }
    )
    arrival_time: None | str = field(
        default=None,
        metadata={
            "name": "ArrivalTime",
            "type": "Attribute",
        },
    )
    train_number: str = field(
        metadata={
            "name": "TrainNumber",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 8,
        }
    )
    provider_code: str = field(
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        }
    )
    supplier_code: str = field(
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 5,
        }
    )
