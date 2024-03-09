from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.corporate_discount_id_1 import CorporateDiscountId1
from travelport.models.type_element_status_1 import TypeElementStatus1

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class HotelUpsellOffer:
    """Offer data of Hotel which is used to send a Hotel Upsell request and match a
    hotel property in the response.

    Offer is found for a matching qualify.

    Parameters
    ----------
    corporate_discount_id
    rate_plan_type
    key
    el_stat
        This attribute is used to show the action results of an element.
        Possible values are "A" (when elements have been added to the UR)
        and "M" (when existing elements have been modified). Response only.
    key_override
        If a duplicate key is found where we are adding elements in some
        cases like URAdd, then instead of erroring out set this attribute to
        true.
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
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    el_stat: None | TypeElementStatus1 = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        },
    )
    key_override: None | bool = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        },
    )
