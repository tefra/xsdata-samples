from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.hotel_rate_detail import HotelRateDetail
from travelport.models.hotel_rule_item import HotelRuleItem
from travelport.models.hotel_type import HotelType

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class HotelRulesRsp(BaseRsp1):
    """
    Response showing rule details of a given hotel property and room rate code.

    Parameters
    ----------
    hotel_rate_detail
        Returns hotels rate and rule details.
    hotel_rule_item
        Return rules and policies related to the property (Like
        Cancellation, Accepted FOP etc.).
    hotel_type
        Supported Providers:1G/1V/1P.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    hotel_rate_detail: list[HotelRateDetail] = field(
        default_factory=list,
        metadata={
            "name": "HotelRateDetail",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    hotel_rule_item: list[HotelRuleItem] = field(
        default_factory=list,
        metadata={
            "name": "HotelRuleItem",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    hotel_type: None | HotelType = field(
        default=None,
        metadata={
            "name": "HotelType",
            "type": "Element",
        },
    )
