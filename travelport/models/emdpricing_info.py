from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.tax_info import TaxInfo

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class EmdpricingInfo:
    """Fare related information for these electronic miscellaneous documents.

    Supported providers are 1G/1V/1P
    """

    class Meta:
        name = "EMDPricingInfo"
        namespace = "http://www.travelport.com/schema/air_v52_0"

    tax_info: list[TaxInfo] = field(
        default_factory=list,
        metadata={
            "name": "TaxInfo",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    base_fare: None | str = field(
        default=None,
        metadata={
            "name": "BaseFare",
            "type": "Attribute",
        },
    )
    total_fare: None | str = field(
        default=None,
        metadata={
            "name": "TotalFare",
            "type": "Attribute",
        },
    )
    total_tax: None | str = field(
        default=None,
        metadata={
            "name": "TotalTax",
            "type": "Attribute",
        },
    )
    equiv_fare: None | str = field(
        default=None,
        metadata={
            "name": "EquivFare",
            "type": "Attribute",
        },
    )
