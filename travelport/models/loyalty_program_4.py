from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_element_status_5 import TypeElementStatus5

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass
class LoyaltyProgram4:
    """
    Parameters
    ----------
    key
    supplier_code
        The code used to identify the Loyalty supplier, e.g. AA, ZE, MC
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
    level
    """

    class Meta:
        name = "LoyaltyProgram"
        namespace = "http://www.travelport.com/schema/common_v37_0"

    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    supplier_code: None | str = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "required": True,
            "length": 2,
        },
    )
    alliance_level: None | str = field(
        default=None,
        metadata={
            "name": "AllianceLevel",
            "type": "Attribute",
        },
    )
    membership_program: None | str = field(
        default=None,
        metadata={
            "name": "MembershipProgram",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 32,
        },
    )
    el_stat: None | TypeElementStatus5 = field(
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
    level: None | object = field(
        default=None,
        metadata={
            "name": "Level",
            "type": "Attribute",
        },
    )
