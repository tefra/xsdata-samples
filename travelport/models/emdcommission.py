from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from travelport.models.type_adjustment_type import TypeAdjustmentType

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class Emdcommission:
    """
    Commission information to be used for EMD issuance.

    Supported providers are 1V/1G/1P.

    Parameters
    ----------
    type_value
        Type of the commission applied.One of Amount/Percentage
    value
        Value of the commission applied for EMD issuance.Could represent
        amount or percentage depending on the type
    currency_code
        Currency of the commission amount applied.Applicable only with type
        - Amount
    """

    class Meta:
        name = "EMDCommission"
        namespace = "http://www.travelport.com/schema/air_v52_0"

    type_value: TypeAdjustmentType = field(
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    value: Decimal = field(
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        }
    )
    currency_code: None | str = field(
        default=None,
        metadata={
            "name": "CurrencyCode",
            "type": "Attribute",
            "length": 3,
        },
    )
