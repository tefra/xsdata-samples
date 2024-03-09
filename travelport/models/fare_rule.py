from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.fare_rule_long import FareRuleLong
from travelport.models.fare_rule_short import FareRuleShort
from travelport.models.rule_advanced_purchase import RuleAdvancedPurchase
from travelport.models.rule_charges import RuleCharges
from travelport.models.rule_length_of_stay import RuleLengthOfStay
from travelport.models.structured_fare_rules_type import (
    StructuredFareRulesType,
)
from travelport.models.type_result_message_1 import TypeResultMessage1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class FareRule:
    """
    Fare Rule Container.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    fare_rule_long: list[FareRuleLong] = field(
        default_factory=list,
        metadata={
            "name": "FareRuleLong",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    fare_rule_short: list[FareRuleShort] = field(
        default_factory=list,
        metadata={
            "name": "FareRuleShort",
            "type": "Element",
            "max_occurs": 999,
        },
    )
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
    fare_rule_result_message: list[TypeResultMessage1] = field(
        default_factory=list,
        metadata={
            "name": "FareRuleResultMessage",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    structured_fare_rules: None | StructuredFareRulesType = field(
        default=None,
        metadata={
            "name": "StructuredFareRules",
            "type": "Element",
        },
    )
    fare_info_ref: None | str = field(
        default=None,
        metadata={
            "name": "FareInfoRef",
            "type": "Attribute",
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
    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        },
    )
    supplier_code: None | str = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        },
    )
