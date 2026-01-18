from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(kw_only=True)
class MeasureType:
    value: float = field(
        metadata={
            "required": True,
        }
    )
    uom: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[^: \n\r\t]+",
        }
    )
