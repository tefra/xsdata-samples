from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.tax_calc_info import TaxCalcInfo

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass(kw_only=True)
class CalculateTaxResult:
    """
    Result container for a tax calculation.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    tax_calc_info: list[TaxCalcInfo] = field(
        default_factory=list,
        metadata={
            "name": "TaxCalcInfo",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    total_base_fare: str = field(
        metadata={
            "name": "TotalBaseFare",
            "type": "Attribute",
            "required": True,
        }
    )
    total_tax: str = field(
        metadata={
            "name": "TotalTax",
            "type": "Attribute",
            "required": True,
        }
    )
    total_fare: str = field(
        metadata={
            "name": "TotalFare",
            "type": "Attribute",
            "required": True,
        }
    )
