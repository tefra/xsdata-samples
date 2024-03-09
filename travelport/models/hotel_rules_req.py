from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_1 import BaseReq1
from travelport.models.hotel_property import HotelProperty
from travelport.models.hotel_rules_lookup_rules_detail_reqd import (
    HotelRulesLookupRulesDetailReqd,
)
from travelport.models.hotel_rules_modifiers import HotelRulesModifiers
from travelport.models.hotel_stay import HotelStay

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class HotelRulesReq(BaseReq1):
    """
    Retrieves hotel rules using hotel property code, chain code and hotel room rate
    type.

    Parameters
    ----------
    hotel_reservation_locator_code
        Request hotel rules using Locator code of existing hotel
        reservation.
    hotel_rules_lookup
        Details to request Hotel rate rules post shopping request.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    hotel_reservation_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "HotelReservationLocatorCode",
            "type": "Element",
            "min_length": 5,
            "max_length": 8,
        },
    )
    hotel_rules_lookup: None | HotelRulesReq.HotelRulesLookup = field(
        default=None,
        metadata={
            "name": "HotelRulesLookup",
            "type": "Element",
        },
    )

    @dataclass
    class HotelRulesLookup:
        """
        Parameters
        ----------
        hotel_property
        hotel_stay
        hotel_rules_modifiers
        rate_plan_type
            This is room rate plan type for a particular rate plan
        base
            This is the Base Amount for the selected rate plan type as
            received in Hotel Details/Book/Modify Response.
        rules_detail_reqd
            Request details for Rules, Details, or All.  Default is All.
            Applicable for 1p.
        """

        hotel_property: None | HotelProperty = field(
            default=None,
            metadata={
                "name": "HotelProperty",
                "type": "Element",
                "required": True,
            },
        )
        hotel_stay: None | HotelStay = field(
            default=None,
            metadata={
                "name": "HotelStay",
                "type": "Element",
                "required": True,
            },
        )
        hotel_rules_modifiers: None | HotelRulesModifiers = field(
            default=None,
            metadata={
                "name": "HotelRulesModifiers",
                "type": "Element",
            },
        )
        rate_plan_type: None | str = field(
            default=None,
            metadata={
                "name": "RatePlanType",
                "type": "Attribute",
                "required": True,
            },
        )
        base: None | str = field(
            default=None,
            metadata={
                "name": "Base",
                "type": "Attribute",
                "required": True,
            },
        )
        rules_detail_reqd: None | HotelRulesLookupRulesDetailReqd = field(
            default=None,
            metadata={
                "name": "RulesDetailReqd",
                "type": "Attribute",
            },
        )
