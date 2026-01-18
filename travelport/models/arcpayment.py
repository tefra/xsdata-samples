from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass(kw_only=True)
class Arcpayment:
    """
    ARC form of payment.ACH Only.

    Parameters
    ----------
    arcidentifier
        Value of the ARC Direct Bill id
    arcpassword
        Value of the ARC Direct Bill id password
    """

    class Meta:
        name = "ARCPayment"
        namespace = "http://www.travelport.com/schema/common_v52_0"

    arcidentifier: str = field(
        metadata={
            "name": "ARCIdentifier",
            "type": "Attribute",
            "required": True,
            "max_length": 128,
        }
    )
    arcpassword: None | str = field(
        default=None,
        metadata={
            "name": "ARCPassword",
            "type": "Attribute",
            "max_length": 128,
        },
    )
