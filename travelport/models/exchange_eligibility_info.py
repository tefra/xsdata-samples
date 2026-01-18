from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.exchange_penalty_info import ExchangePenaltyInfo

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class ExchangeEligibilityInfo:
    """
    Parameters
    ----------
    exchange_penalty_info
    eligible_fares
        Identifies which fares are eligible for Exchange
    refundable_fares
        Fares eligible for refund: All, Some, None
    passed_automation_checks
        Indicates whether the itinerary passed initial validation for
        automated exchange
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    exchange_penalty_info: list[ExchangePenaltyInfo] = field(
        default_factory=list,
        metadata={
            "name": "ExchangePenaltyInfo",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    eligible_fares: None | str = field(
        default=None,
        metadata={
            "name": "EligibleFares",
            "type": "Attribute",
        },
    )
    refundable_fares: None | str = field(
        default=None,
        metadata={
            "name": "RefundableFares",
            "type": "Attribute",
        },
    )
    passed_automation_checks: None | bool = field(
        default=None,
        metadata={
            "name": "PassedAutomationChecks",
            "type": "Attribute",
        },
    )
