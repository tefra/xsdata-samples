from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class FareComponentBreakdownType:
    """
    Fare Component Breakdown.

    Attributes:
        fare_component_reference_id:
        fare_component_commission: Commission Amount per Fare Component
        rule_id: Commission Rule ID
        program_id: Commission Program ID
        contract_id: Commission Contract ID
    """

    fare_component_reference_id: None | int = field(
        default=None,
        metadata={
            "name": "FareComponentReferenceID",
            "type": "Attribute",
        },
    )
    fare_component_commission: None | Decimal = field(
        default=None,
        metadata={
            "name": "FareComponentCommission",
            "type": "Attribute",
            "fraction_digits": 3,
        },
    )
    rule_id: None | int = field(
        default=None,
        metadata={
            "name": "RuleID",
            "type": "Attribute",
        },
    )
    program_id: None | int = field(
        default=None,
        metadata={
            "name": "ProgramID",
            "type": "Attribute",
        },
    )
    contract_id: None | int = field(
        default=None,
        metadata={
            "name": "ContractID",
            "type": "Attribute",
        },
    )
