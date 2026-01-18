from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass(kw_only=True)
class TypeRateVariance:
    """
    Parameters
    ----------
    type_value
        Supported values are 'percentage.1P. Future release 'amopunt'.
    value
        Represents value of user permitted variance for sell success. eg.
        "5.00" = 5%  variance on the supplier estimated total amount
        response will be successful. 1P.
    apply
        Variance to response amount;  'high', 'low' or 'both. 1P.
    """

    class Meta:
        name = "typeRateVariance"

    type_value: str = field(
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
    apply: str = field(
        metadata={
            "name": "Apply",
            "type": "Attribute",
            "required": True,
        }
    )
