from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class RuleCharges:
    """
    Container for rules related to charges such as deposits, surcharges,
    penalities, etc..

    Parameters
    ----------
    penalty_type
    departure_status
    amount
    percent
    more_rules_present
        If true, specifies that advance purchase information will be present
        in fare rules.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    penalty_type: None | str = field(
        default=None,
        metadata={
            "name": "PenaltyType",
            "type": "Attribute",
        },
    )
    departure_status: None | str = field(
        default=None,
        metadata={
            "name": "DepartureStatus",
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
    percent: None | Decimal = field(
        default=None,
        metadata={
            "name": "Percent",
            "type": "Attribute",
        },
    )
    more_rules_present: None | bool = field(
        default=None,
        metadata={
            "name": "MoreRulesPresent",
            "type": "Attribute",
        },
    )
