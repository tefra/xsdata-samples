from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_add import AirAdd
from travelport.models.air_delete import AirDelete
from travelport.models.air_update import AirUpdate
from travelport.models.hotel_add import HotelAdd
from travelport.models.hotel_delete import HotelDelete
from travelport.models.hotel_update import HotelUpdate
from travelport.models.passive_add import PassiveAdd
from travelport.models.passive_delete import PassiveDelete
from travelport.models.rail_update import RailUpdate
from travelport.models.universal_add import UniversalAdd
from travelport.models.universal_delete import UniversalDelete
from travelport.models.universal_update import UniversalUpdate
from travelport.models.vehicle_add import VehicleAdd
from travelport.models.vehicle_delete import VehicleDelete
from travelport.models.vehicle_update import VehicleUpdate

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass(kw_only=True)
class UniversalModifyCmd:
    """
    Container for the elements that will be batch updated to a
    UniversalRecord.

    Parameters
    ----------
    vehicle_add
    vehicle_delete
    vehicle_update
    air_add
    air_delete
    air_update
    universal_add
    universal_delete
    universal_update
    hotel_add
    hotel_update
    hotel_delete
    passive_add
    passive_delete
    rail_update
    key
        Refers the universal modify command key. It should be unique in the
        request.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    vehicle_add: None | VehicleAdd = field(
        default=None,
        metadata={
            "name": "VehicleAdd",
            "type": "Element",
        },
    )
    vehicle_delete: None | VehicleDelete = field(
        default=None,
        metadata={
            "name": "VehicleDelete",
            "type": "Element",
        },
    )
    vehicle_update: None | VehicleUpdate = field(
        default=None,
        metadata={
            "name": "VehicleUpdate",
            "type": "Element",
        },
    )
    air_add: None | AirAdd = field(
        default=None,
        metadata={
            "name": "AirAdd",
            "type": "Element",
        },
    )
    air_delete: None | AirDelete = field(
        default=None,
        metadata={
            "name": "AirDelete",
            "type": "Element",
        },
    )
    air_update: None | AirUpdate = field(
        default=None,
        metadata={
            "name": "AirUpdate",
            "type": "Element",
        },
    )
    universal_add: None | UniversalAdd = field(
        default=None,
        metadata={
            "name": "UniversalAdd",
            "type": "Element",
        },
    )
    universal_delete: None | UniversalDelete = field(
        default=None,
        metadata={
            "name": "UniversalDelete",
            "type": "Element",
        },
    )
    universal_update: None | UniversalUpdate = field(
        default=None,
        metadata={
            "name": "UniversalUpdate",
            "type": "Element",
        },
    )
    hotel_add: None | HotelAdd = field(
        default=None,
        metadata={
            "name": "HotelAdd",
            "type": "Element",
        },
    )
    hotel_update: None | HotelUpdate = field(
        default=None,
        metadata={
            "name": "HotelUpdate",
            "type": "Element",
        },
    )
    hotel_delete: None | HotelDelete = field(
        default=None,
        metadata={
            "name": "HotelDelete",
            "type": "Element",
        },
    )
    passive_add: None | PassiveAdd = field(
        default=None,
        metadata={
            "name": "PassiveAdd",
            "type": "Element",
        },
    )
    passive_delete: None | PassiveDelete = field(
        default=None,
        metadata={
            "name": "PassiveDelete",
            "type": "Element",
        },
    )
    rail_update: None | RailUpdate = field(
        default=None,
        metadata={
            "name": "RailUpdate",
            "type": "Element",
        },
    )
    key: str = field(
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
