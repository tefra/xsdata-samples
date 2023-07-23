from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class Bsppayment:
    """
    BSP form of payment.ACH Only.

    Parameters
    ----------
    bspidentifier
        Value of the BSP Direct Bill id
    bsppassword
        Value of the BSP Direct Bill id password
    """
    class Meta:
        name = "BSPPayment"
        namespace = "http://www.travelport.com/schema/common_v52_0"

    bspidentifier: None | str = field(
        default=None,
        metadata={
            "name": "BSPIdentifier",
            "type": "Attribute",
            "required": True,
            "max_length": 128,
        }
    )
    bsppassword: None | str = field(
        default=None,
        metadata={
            "name": "BSPPassword",
            "type": "Attribute",
            "max_length": 128,
        }
    )
