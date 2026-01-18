from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass(kw_only=True)
class ServiceFeeTaxInfo5:
    """
    The taxes associated to a particular Service Fee.

    Parameters
    ----------
    category
        The tax category represents a valid IATA tax code.
    amount
    """

    class Meta:
        name = "ServiceFeeTaxInfo"
        namespace = "http://www.travelport.com/schema/common_v34_0"

    category: str = field(
        metadata={
            "name": "Category",
            "type": "Attribute",
            "required": True,
        }
    )
    amount: str = field(
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "required": True,
        }
    )
