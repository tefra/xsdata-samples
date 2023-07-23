from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_tax_info_5 import TypeTaxInfo5

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class McopriceData5:
    """
    Parameters
    ----------
    tax_info
    commission
    mcoamount
        The total value of the MCO including any processing fees.
    mcoequivalent_fare
        Exchange value of the currency actually collected.
    mcototal_amount
        The Total amount for the MCO.
    """
    class Meta:
        name = "MCOPriceData"
        namespace = "http://www.travelport.com/schema/common_v34_0"

    tax_info: list[TypeTaxInfo5] = field(
        default_factory=list,
        metadata={
            "name": "TaxInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    commission: None | McopriceData5.Commission = field(
        default=None,
        metadata={
            "name": "Commission",
            "type": "Element",
        }
    )
    mcoamount: None | str = field(
        default=None,
        metadata={
            "name": "MCOAmount",
            "type": "Attribute",
            "required": True,
        }
    )
    mcoequivalent_fare: None | str = field(
        default=None,
        metadata={
            "name": "MCOEquivalentFare",
            "type": "Attribute",
        }
    )
    mcototal_amount: None | str = field(
        default=None,
        metadata={
            "name": "MCOTotalAmount",
            "type": "Attribute",
        }
    )

    @dataclass
    class Commission:
        """
        Parameters
        ----------
        amount
            The monetary amount.
        percentage
            The percentage.
        """
        amount: None | str = field(
            default=None,
            metadata={
                "name": "Amount",
                "type": "Attribute",
            }
        )
        percentage: None | str = field(
            default=None,
            metadata={
                "name": "Percentage",
                "type": "Attribute",
                "pattern": r"([0-9]{1,2}|100)\.[0-9]{1,2}",
            }
        )
