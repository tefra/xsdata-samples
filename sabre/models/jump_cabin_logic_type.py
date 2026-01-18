from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class JumpCabinLogicType:
    """
    Attributes:
        disabled: Controls if response could contain options with cabin
            class different than requested.
    """

    disabled: bool = field(
        metadata={
            "name": "Disabled",
            "type": "Attribute",
            "required": True,
        }
    )
