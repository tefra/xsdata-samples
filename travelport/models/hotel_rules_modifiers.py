from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.corporate_discount_id_1 import CorporateDiscountId1
from travelport.models.hotel_bedding import HotelBedding
from travelport.models.number_of_children import NumberOfChildren
from travelport.models.permitted_providers_1 import PermittedProviders1

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class HotelRulesModifiers:
    """
    Controls and switches for the Hotel Rules request.

    Parameters
    ----------
    permitted_providers
    number_of_children
    hotel_bedding
    rate_category
        Specify Rate Category
    corporate_discount_id
    number_of_adults
        Defaults to 1 if not specified
    number_of_rooms
        The numbers of rooms,defaults to 1 if not specified
    total_occupants
        Number of guests for the room.  Supported Providers: 1P
    key
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    permitted_providers: None | PermittedProviders1 = field(
        default=None,
        metadata={
            "name": "PermittedProviders",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    number_of_children: None | NumberOfChildren = field(
        default=None,
        metadata={
            "name": "NumberOfChildren",
            "type": "Element",
        },
    )
    hotel_bedding: list[HotelBedding] = field(
        default_factory=list,
        metadata={
            "name": "HotelBedding",
            "type": "Element",
            "max_occurs": 4,
        },
    )
    rate_category: None | int = field(
        default=None,
        metadata={
            "name": "RateCategory",
            "type": "Element",
        },
    )
    corporate_discount_id: list[CorporateDiscountId1] = field(
        default_factory=list,
        metadata={
            "name": "CorporateDiscountID",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 2,
        },
    )
    number_of_adults: None | int = field(
        default=None,
        metadata={
            "name": "NumberOfAdults",
            "type": "Attribute",
        },
    )
    number_of_rooms: int = field(
        default=1,
        metadata={
            "name": "NumberOfRooms",
            "type": "Attribute",
        },
    )
    total_occupants: None | int = field(
        default=None,
        metadata={
            "name": "TotalOccupants",
            "type": "Attribute",
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
