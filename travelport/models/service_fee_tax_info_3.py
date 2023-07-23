from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class ServiceFeeTaxInfo3:
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
        namespace = "http://www.travelport.com/schema/common_v33_0"

    category: None | str = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
            "required": True,
        }
    )
    amount: None | str = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "required": True,
        }
    )
