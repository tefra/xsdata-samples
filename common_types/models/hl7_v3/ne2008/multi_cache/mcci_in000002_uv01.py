from __future__ import annotations

from dataclasses import dataclass, field

from .mcci_mt000200_uv01 import McciMt000200Uv01Message

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class McciIn000002Uv01(McciMt000200Uv01Message):
    class Meta:
        name = "MCCI_IN000002UV01"
        namespace = "urn:hl7-org:v3"

    itsversion: str = field(
        init=False,
        default="XML_1.0",
        metadata={
            "name": "ITSVersion",
            "type": "Attribute",
            "required": True,
        },
    )
