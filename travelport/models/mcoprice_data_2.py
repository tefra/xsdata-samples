from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_tax_info_2 import TypeTaxInfo2

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass(kw_only=True)
class McopriceData2:
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
        namespace = "http://www.travelport.com/schema/common_v32_0"

    tax_info: list[TypeTaxInfo2] = field(
        default_factory=list,
        metadata={
            "name": "TaxInfo",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    commission: None | McopriceData2.Commission = field(
        default=None,
        metadata={
            "name": "Commission",
            "type": "Element",
        },
    )
    mcoamount: str = field(
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
        },
    )
    mcototal_amount: None | str = field(
        default=None,
        metadata={
            "name": "MCOTotalAmount",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
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
            },
        )
        percentage: None | str = field(
            default=None,
            metadata={
                "name": "Percentage",
                "type": "Attribute",
                "pattern": r"([0-9]{1,2}|100)\.[0-9]{1,2}",
            },
        )
