from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.rule_advanced_purchase import RuleAdvancedPurchase
from travelport.models.rule_charges import RuleCharges
from travelport.models.rule_length_of_stay import RuleLengthOfStay

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class FareDisplayRule:
    """
    Fare Display Rule Container.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    rule_advanced_purchase: None | RuleAdvancedPurchase = field(
        default=None,
        metadata={
            "name": "RuleAdvancedPurchase",
            "type": "Element",
        },
    )
    rule_length_of_stay: None | RuleLengthOfStay = field(
        default=None,
        metadata={
            "name": "RuleLengthOfStay",
            "type": "Element",
        },
    )
    rule_charges: None | RuleCharges = field(
        default=None,
        metadata={
            "name": "RuleCharges",
            "type": "Element",
        },
    )
    rule_number: None | str = field(
        default=None,
        metadata={
            "name": "RuleNumber",
            "type": "Attribute",
        },
    )
    source: None | str = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Attribute",
        },
    )
    tariff_number: None | str = field(
        default=None,
        metadata={
            "name": "TariffNumber",
            "type": "Attribute",
        },
    )
