from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_carrier_code import TypeCarrierCode

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class IncludeAddlBookingCodeInfo:
    """
    Used to include primary or secondary carrier's booking code details.

    Parameters
    ----------
    type_value
        The type defines that the booking code info is for primary or
        secondary carrier.
    secondary_carrier
        The secondary carrier code is required when type is secondary .
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    type_value: None | TypeCarrierCode = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    secondary_carrier: None | str = field(
        default=None,
        metadata={
            "name": "SecondaryCarrier",
            "type": "Attribute",
            "length": 2,
        }
    )
