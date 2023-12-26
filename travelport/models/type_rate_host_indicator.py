from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class TypeRateHostIndicator:
    """
    Host-specific info for vendors.

    Parameters
    ----------
    inventory_token
        Vendor info about rate to adjust pricing as needed
    rate_token
        Assocates shop response to sell request
    """

    class Meta:
        name = "typeRateHostIndicator"

    inventory_token: None | str = field(
        default=None,
        metadata={
            "name": "InventoryToken",
            "type": "Attribute",
        },
    )
    rate_token: None | str = field(
        default=None,
        metadata={
            "name": "RateToken",
            "type": "Attribute",
        },
    )
