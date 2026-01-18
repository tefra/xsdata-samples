from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class LoyaltyCardDetails:
    """
    Passenger Loyalty card details.

    Parameters
    ----------
    supplier_code
        Carrier Code
    priority_code
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    supplier_code: str = field(
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "required": True,
            "length": 2,
        }
    )
    priority_code: str = field(
        metadata={
            "name": "PriorityCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-zA-Z0-9]{1,1}",
        }
    )
