from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class TaxCalcInfo:
    """
    Container for a single segment for tax calculation purposes.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    origin: None | str = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    destination: None | str = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    base_fare: None | str = field(
        default=None,
        metadata={
            "name": "BaseFare",
            "type": "Attribute",
            "required": True,
        }
    )
    qsurcharge: None | str = field(
        default=None,
        metadata={
            "name": "QSurcharge",
            "type": "Attribute",
        }
    )
    stop_over_fee: None | str = field(
        default=None,
        metadata={
            "name": "StopOverFee",
            "type": "Attribute",
        }
    )
    tax: None | str = field(
        default=None,
        metadata={
            "name": "Tax",
            "type": "Attribute",
        }
    )
