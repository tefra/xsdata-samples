from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.tax_info import TaxInfo

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class PrePayPriceInfo:
    """
    Pricing detail for the Pre Pay Account.

    Parameters
    ----------
    tax_info
        Detailed tax information for the pre pay account
    base_fare
    total_fare
    total_tax
    """

    class Meta:
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
