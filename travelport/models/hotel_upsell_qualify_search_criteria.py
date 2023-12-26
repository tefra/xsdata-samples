from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.corporate_discount_id_1 import CorporateDiscountId1
from travelport.models.upsell_search_criteria import UpsellSearchCriteria

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class HotelUpsellQualifySearchCriteria(UpsellSearchCriteria):
    """
    Search criteria for HotelUpsellQualify.

    Parameters
    ----------
    corporate_discount_id
    hotel_chain_code
    hotel_code
    hotel_location
        The IATA location code for this entity.
    rate_plan_type
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    corporate_discount_id: None | CorporateDiscountId1 = field(
        default=None,
        metadata={
            "name": "CorporateDiscountID",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    hotel_chain_code: None | str = field(
        default=None,
        metadata={
            "name": "HotelChainCode",
            "type": "Attribute",
            "required": True,
            "length": 2,
        },
    )
    hotel_code: None | str = field(
        default=None,
        metadata={
            "name": "HotelCode",
            "type": "Attribute",
            "max_length": 32,
        },
    )
    hotel_location: None | str = field(
        default=None,
        metadata={
            "name": "HotelLocation",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        },
    )
    rate_plan_type: None | str = field(
        default=None,
        metadata={
            "name": "RatePlanType",
            "type": "Attribute",
        },
    )
