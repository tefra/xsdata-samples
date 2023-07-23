from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_element_status_3 import TypeElementStatus3
from travelport.models.type_product_2 import TypeProduct2
from travelport.models.type_provider_reservation_specific_info_2 import TypeProviderReservationSpecificInfo2

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass
class LoyaltyCard2:
    """
    Provider loyalty card information.

    Parameters
    ----------
    provider_reservation_specific_info
    key
    supplier_code
        Carrier Code
    alliance_level
    membership_program
        Loyalty Program membership Id of the traveler specific to Amtrak(2V)
        Guest Rewards
    el_stat
        This attribute is used to show the action results of an element.
        Possible values are "A" (when elements have been added to the UR)
        and "M" (when existing elements have been modified). Response only.
    key_override
        If a duplicate key is found where we are adding elements in some
        cases like URAdd, then instead of erroring out set this attribute to
        true.
    card_number
    status
    membership_status
    free_text
    supplier_type
    level
    priority_code
    vendor_location_ref
    """
    class Meta:
        name = "LoyaltyCard"
        namespace = "http://www.travelport.com/schema/common_v32_0"

    provider_reservation_specific_info: list[TypeProviderReservationSpecificInfo2] = field(
        default_factory=list,
        metadata={
            "name": "ProviderReservationSpecificInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    supplier_code: None | str = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "required": True,
            "length": 2,
        }
    )
    alliance_level: None | str = field(
        default=None,
        metadata={
            "name": "AllianceLevel",
            "type": "Attribute",
        }
    )
    membership_program: None | str = field(
        default=None,
        metadata={
            "name": "MembershipProgram",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 32,
        }
    )
    el_stat: None | TypeElementStatus3 = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: None | bool = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )
    card_number: None | str = field(
        default=None,
        metadata={
            "name": "CardNumber",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 36,
        }
    )
    status: None | str = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
        }
    )
    membership_status: None | str = field(
        default=None,
        metadata={
            "name": "MembershipStatus",
            "type": "Attribute",
        }
    )
    free_text: None | str = field(
        default=None,
        metadata={
            "name": "FreeText",
            "type": "Attribute",
        }
    )
    supplier_type: None | TypeProduct2 = field(
        default=None,
        metadata={
            "name": "SupplierType",
            "type": "Attribute",
        }
    )
    level: None | str = field(
        default=None,
        metadata={
            "name": "Level",
            "type": "Attribute",
            "pattern": r"[a-zA-Z0-9]{1,1}",
        }
    )
    priority_code: None | str = field(
        default=None,
        metadata={
            "name": "PriorityCode",
            "type": "Attribute",
            "pattern": r"[a-zA-Z0-9]{1,1}",
        }
    )
    vendor_location_ref: None | str = field(
        default=None,
        metadata={
            "name": "VendorLocationRef",
            "type": "Attribute",
        }
    )
