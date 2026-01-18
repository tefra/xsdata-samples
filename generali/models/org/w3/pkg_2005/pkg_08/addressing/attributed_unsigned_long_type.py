from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.w3.org/2005/08/addressing"


@dataclass(kw_only=True)
class AttributedUnsignedLongType:
    value: int = field(
        metadata={
            "required": True,
        }
    )
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
