from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.agency_sell_info_1 import AgencySellInfo1
from travelport.models.air_segment import AirSegment
from travelport.models.base_req_1 import BaseReq1
from travelport.models.host_reservation import HostReservation
from travelport.models.host_token_1 import HostToken1
from travelport.models.merchandising_pricing_modifiers import MerchandisingPricingModifiers
from travelport.models.search_traveler import SearchTraveler

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class SeatMapReq(BaseReq1):
    """
    Request a seat map for the give flight information.

    Parameters
    ----------
    agency_sell_info
        Provider: ACH-Required if the user requesting the seat map is not
        the same agent authenticated in the request.
    air_segment
        Provider: 1G,1V,1P,ACH,MCH.
    host_token
        Provider: ACH-Required if the carrier has multiple adapters.
    search_traveler
        Provider: 1G,1V,ACH,MCH.
    host_reservation
        Provider: ACH,MCH-Required when seat price is requested.
    merchandising_pricing_modifiers
        Used to provide additional pricing options. Provider:ACH.
    return_seat_pricing
        Provider: 1G,1V,1P,ACH-When set to true the price of the seat will
        be returned if it exists.
    return_branding_info
        A value of true will return the BrandingInfo block in the response
        if applicable. A value of false will not return the BrandingInfo
        block in the response. Providers: 1G, 1V, 1P, ACH
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    agency_sell_info: None | AgencySellInfo1 = field(
        default=None,
        metadata={
            "name": "AgencySellInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    air_segment: list[AirSegment] = field(
        default_factory=list,
        metadata={
            "name": "AirSegment",
            "type": "Element",
            "max_occurs": 99,
        }
    )
    host_token: list[HostToken1] = field(
        default_factory=list,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 99,
        }
    )
    search_traveler: list[SearchTraveler] = field(
        default_factory=list,
        metadata={
            "name": "SearchTraveler",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    host_reservation: None | HostReservation = field(
        default=None,
        metadata={
            "name": "HostReservation",
            "type": "Element",
        }
    )
    merchandising_pricing_modifiers: None | MerchandisingPricingModifiers = field(
        default=None,
        metadata={
            "name": "MerchandisingPricingModifiers",
            "type": "Element",
        }
    )
    return_seat_pricing: None | bool = field(
        default=None,
        metadata={
            "name": "ReturnSeatPricing",
            "type": "Attribute",
            "required": True,
        }
    )
    return_branding_info: bool = field(
        default=False,
        metadata={
            "name": "ReturnBrandingInfo",
            "type": "Attribute",
        }
    )
