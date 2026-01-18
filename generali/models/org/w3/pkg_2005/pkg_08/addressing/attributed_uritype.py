from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.w3.org/2005/08/addressing"


@dataclass
class AttributedUritype:
    class Meta:
        name = "AttributedURIType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
