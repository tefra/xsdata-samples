from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_fare_penalty_penalty_applies import TypeFarePenaltyPenaltyApplies

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class TypeFarePenalty:
    """
    Penalty applicable on a Fare for change/ cancellation etc- expressed in both
    Money and Percentage.

    Parameters
    ----------
    amount
        The penalty (if any) - expressed as the actual amount of money. Both
        Amount and Percentage can be present.
    percentage
        The penalty (if any) - expressed in percentage. Both Amount and
        Percentage can be present.
    penalty_applies
    no_show
        The No Show penalty (if any) to change/cancel the fare.
    """
    class Meta:
        name = "typeFarePenalty"

    amount: None | str = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    percentage: None | str = field(
        default=None,
        metadata={
            "name": "Percentage",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "pattern": r"([0-9]{1,2}|100)\.[0-9]{1,2}",
        }
    )
    penalty_applies: None | TypeFarePenaltyPenaltyApplies = field(
        default=None,
        metadata={
            "name": "PenaltyApplies",
            "type": "Attribute",
        }
    )
    no_show: None | bool = field(
        default=None,
        metadata={
            "name": "NoShow",
            "type": "Attribute",
        }
    )
