from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.corporate_discount_id_1 import CorporateDiscountId1
from travelport.models.type_element_status_1 import TypeElementStatus1

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class HotelUpsellQualify:
    """Qualify data of Hotel against which Hotel property details search is matched
    to get an upsell Offer.

    Each qualify should have an offer.

    Parameters
    ----------
    corporate_discount_id
    hotel_chain_code
    hotel_code
    hotel_location
        The IATA location code for this entity.
    rate_plan_type
    effective_date
    expiration_date
    key
    el_stat
        This attribute is used to show the action results of an element.
        Possible values are "A" (when elements have been added to the UR)
        and "M" (when existing elements have been modified). Response only.
    key_override
        If a duplicate key is found where we are adding elements in some
        cases like URAdd, then instead of erroring out set this attribute to
        true.
    offer_ref
        Reference to the Offer.
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
    effective_date: None | str = field(
        default=None,
        metadata={
            "name": "EffectiveDate",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^:Z].*",
        },
    )
    expiration_date: None | str = field(
        default=None,
        metadata={
            "name": "ExpirationDate",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^:Z].*",
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
    offer_ref: None | str = field(
        default=None,
        metadata={
            "name": "OfferRef",
            "type": "Attribute",
        },
    )
