from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

__NAMESPACE__ = "http://www.w3.org/2005/08/addressing"


@dataclass
class AttributedQnameType:
    class Meta:
        name = "AttributedQNameType"

    value: None | QName = field(
        default=None,
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
