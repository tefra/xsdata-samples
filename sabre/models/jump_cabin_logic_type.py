from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class JumpCabinLogicType:
    """
    Attributes:
        disabled: Controls if response could contain options with cabin
            class different than requested.
    """

    disabled: None | bool = field(
        default=None,
        metadata={
            "name": "Disabled",
            "type": "Attribute",
            "required": True,
        },
    )
