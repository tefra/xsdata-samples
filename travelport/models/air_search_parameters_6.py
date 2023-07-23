from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass
class AirSearchParameters6:
    """
    Search Parameters.
    """
    class Meta:
        name = "AirSearchParameters"
        namespace = "http://www.travelport.com/schema/common_v38_0"

    no_advance_purchase: None | bool = field(
        default=None,
        metadata={
            "name": "NoAdvancePurchase",
            "type": "Attribute",
        }
    )
    refundable_fares: None | bool = field(
        default=None,
        metadata={
            "name": "RefundableFares",
            "type": "Attribute",
        }
    )
    non_penalty_fares: None | bool = field(
        default=None,
        metadata={
            "name": "NonPenaltyFares",
            "type": "Attribute",
        }
    )
    un_restricted_fares: None | bool = field(
        default=None,
        metadata={
            "name": "UnRestrictedFares",
            "type": "Attribute",
        }
    )
