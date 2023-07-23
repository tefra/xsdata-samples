from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class Tax1:
    """
    Taxes for Land Charges.

    Parameters
    ----------
    category
        The tax category represents a valid IATA tax code.
    amount
    """
    class Meta:
        name = "Tax"
        namespace = "http://www.travelport.com/schema/air_v52_0"

    category: None | str = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
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
