from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class PriceChangeType:
    """
    Indicates a price change is found in Fare Control Manager.

    Parameters
    ----------
    value
    amount
        Contains the currency and amount information. Assume the amount is
        added unless a hyphen is present to indicate subtraction.
    carrier
        Contains carrier code information
    segment_ref
        Contains segment reference information
    """
    value: str = field(
        default="",
        metadata={
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
    carrier: None | str = field(
        default=None,
        metadata={
            "name": "Carrier",
            "type": "Attribute",
        }
    )
    segment_ref: None | str = field(
        default=None,
        metadata={
            "name": "SegmentRef",
            "type": "Attribute",
        }
    )
