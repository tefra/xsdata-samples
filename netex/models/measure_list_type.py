from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(kw_only=True)
class MeasureListType:
    value: Iterable[float] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
    uom: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[^: \n\r\t]+",
        }
    )
