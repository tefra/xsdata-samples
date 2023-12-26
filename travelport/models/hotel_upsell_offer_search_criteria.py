from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.corporate_discount_id_1 import CorporateDiscountId1

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class HotelUpsellOfferSearchCriteria:
    """
    Search criteria for HotelUpsellOffer.
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
    rate_plan_type: None | str = field(
        default=None,
        metadata={
            "name": "RatePlanType",
            "type": "Attribute",
            "required": True,
        },
    )
