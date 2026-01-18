from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from sabre.models.tax_code_type import TaxCodeType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class TaxCodeAmountType(TaxCodeType):
    """
    Defines the data fields available for tax code and amount.
    """

    amount: None | Decimal = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "fraction_digits": 3,
        },
    )
