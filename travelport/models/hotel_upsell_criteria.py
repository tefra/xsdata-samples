from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.hotel_upsell_add import HotelUpsellAdd
from travelport.models.hotel_upsell_delete import HotelUpsellDelete
from travelport.models.hotel_upsell_update import HotelUpsellUpdate

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class HotelUpsellCriteria:
    """
    Wraps all Upsell Admin commands related to Hotel.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    hotel_upsell_add: list[HotelUpsellAdd] = field(
        default_factory=list,
        metadata={
            "name": "HotelUpsellAdd",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    hotel_upsell_update: list[HotelUpsellUpdate] = field(
        default_factory=list,
        metadata={
            "name": "HotelUpsellUpdate",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    hotel_upsell_delete: list[HotelUpsellDelete] = field(
        default_factory=list,
        metadata={
            "name": "HotelUpsellDelete",
            "type": "Element",
            "max_occurs": 999,
        },
    )
