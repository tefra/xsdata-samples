from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_commission_level_4 import TypeCommissionLevel4
from travelport.models.type_commission_modifier_4 import (
    TypeCommissionModifier4,
)
from travelport.models.type_commission_type_4 import TypeCommissionType4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass
class Commission7:
    """
    Identifies the agency commission.

    Parameters
    ----------
    key
    level
        The commission percentage level.
    type_value
        The commission type.
    modifier
        Optional commission modifier.
    amount
        The monetary amount of the commission.
    value
        Contains alphanumeric or alpha characters intended as 1G Value Code
        as applicable by BSP of client.
    percentage
        The percent of the commission.
    booking_traveler_ref
        A reference to a passenger.
    commission_override
        This is enabled to override CAT-35 commission error during air
        ticketing. PROVIDER SUPPORTED:Worldspan and JAL
    """

    class Meta:
        name = "Commission"
        namespace = "http://www.travelport.com/schema/common_v37_0"

    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    level: None | TypeCommissionLevel4 = field(
        default=None,
        metadata={
            "name": "Level",
            "type": "Attribute",
            "required": True,
        },
    )
    type_value: None | TypeCommissionType4 = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        },
    )
    modifier: None | TypeCommissionModifier4 = field(
        default=None,
        metadata={
            "name": "Modifier",
            "type": "Attribute",
        },
    )
    amount: None | str = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
        },
    )
    value: None | str = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "min_length": 0,
            "max_length": 15,
        },
    )
    percentage: None | str = field(
        default=None,
        metadata={
            "name": "Percentage",
            "type": "Attribute",
            "pattern": r"([0-9]{1,2}|100)\.[0-9]{1,2}",
        },
    )
    booking_traveler_ref: None | str = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
        },
    )
    commission_override: bool = field(
        default=False,
        metadata={
            "name": "CommissionOverride",
            "type": "Attribute",
        },
    )
