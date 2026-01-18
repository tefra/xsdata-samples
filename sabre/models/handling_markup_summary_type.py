from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class HandlingMarkupSummaryType:
    """
    Attributes:
        type_code: Value M: Embedded Mark Up, J: Adjusted Selling, H:
            Handling Fee, G: GST Taxes
        description: Max 10 chars
        monetary_amount_value: Can be negative. This is in equivalent
            amount currency.
    """

    type_code: str = field(
        metadata={
            "name": "TypeCode",
            "type": "Attribute",
            "required": True,
            "length": 1,
        }
    )
    description: str = field(
        metadata={
            "name": "Description",
            "type": "Attribute",
            "required": True,
        }
    )
    monetary_amount_value: Decimal = field(
        metadata={
            "name": "MonetaryAmountValue",
            "type": "Attribute",
            "required": True,
            "fraction_digits": 3,
        }
    )
