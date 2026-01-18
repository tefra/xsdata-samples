from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass(kw_only=True)
class CurrencyConversion:
    """
    Parameters
    ----------
    from_value
        From Currency Value for the Conversion
    to
        To Currency Value for the Conversion
    original_amount
        Amount to be converted
    converted_amount
        Amount after the convertion
    bank_selling_rate
        Currency Conversion Rate
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    from_value: str = field(
        metadata={
            "name": "From",
            "type": "Attribute",
            "required": True,
            "length": 3,
        }
    )
    to: str = field(
        metadata={
            "name": "To",
            "type": "Attribute",
            "required": True,
            "length": 3,
        }
    )
    original_amount: None | float = field(
        default=None,
        metadata={
            "name": "OriginalAmount",
            "type": "Attribute",
        },
    )
    converted_amount: None | float = field(
        default=None,
        metadata={
            "name": "ConvertedAmount",
            "type": "Attribute",
        },
    )
    bank_selling_rate: None | float = field(
        default=None,
        metadata={
            "name": "BankSellingRate",
            "type": "Attribute",
        },
    )
