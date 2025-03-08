from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from sabre.models.fare_component_breakdown_type import (
    FareComponentBreakdownType,
)

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class VccinformationType:
    """
    Validating Carrier Commission Information.

    Attributes:
        fare_component_breakdown:
        validating_carrier:
        commission_amount: Commission Amount (in equivalent amount
            currency)
        total_amount_including_mark_up: Total Commision amount including
            Mark-Up
        commission_percent:
    """

    class Meta:
        name = "VCCInformationType"

    fare_component_breakdown: list[FareComponentBreakdownType] = field(
        default_factory=list,
        metadata={
            "name": "FareComponentBreakdown",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 24,
        },
    )
    validating_carrier: None | str = field(
        default=None,
        metadata={
            "name": "ValidatingCarrier",
            "type": "Attribute",
            "pattern": r"[0-9A-Z]{2,3}",
        },
    )
    commission_amount: None | Decimal = field(
        default=None,
        metadata={
            "name": "CommissionAmount",
            "type": "Attribute",
            "required": True,
            "fraction_digits": 3,
        },
    )
    total_amount_including_mark_up: None | Decimal = field(
        default=None,
        metadata={
            "name": "TotalAmountIncludingMarkUp",
            "type": "Attribute",
            "fraction_digits": 3,
        },
    )
    commission_percent: None | Decimal = field(
        default=None,
        metadata={
            "name": "CommissionPercent",
            "type": "Attribute",
            "fraction_digits": 3,
        },
    )
