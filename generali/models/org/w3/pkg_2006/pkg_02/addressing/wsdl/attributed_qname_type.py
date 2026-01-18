from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName

__NAMESPACE__ = "http://www.w3.org/2006/02/addressing/wsdl"


@dataclass
class AttributedQnameType:
    class Meta:
        name = "AttributedQNameType"

    value: QName | None = field(
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
