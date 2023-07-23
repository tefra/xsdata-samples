from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_fare_penalty import TypeFarePenalty

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class PenaltyFareInformation:
    """
    Parameters
    ----------
    penalty_info
        Penalty Limit if requested.
    prohibit_penalty_fares
        Indicates whether user wants penalty fares to be returned.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    penalty_info: None | TypeFarePenalty = field(
        default=None,
        metadata={
            "name": "PenaltyInfo",
            "type": "Element",
        }
    )
    prohibit_penalty_fares: None | bool = field(
        default=None,
        metadata={
            "name": "ProhibitPenaltyFares",
            "type": "Attribute",
            "required": True,
        }
    )
