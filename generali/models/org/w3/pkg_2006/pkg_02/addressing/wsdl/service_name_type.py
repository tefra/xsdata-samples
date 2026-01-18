from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

__NAMESPACE__ = "http://www.w3.org/2006/02/addressing/wsdl"


@dataclass(kw_only=True)
class ServiceNameType:
    value: QName = field(
        metadata={
            "required": True,
        }
    )
    endpoint_name: None | str = field(
        default=None,
        metadata={
            "name": "EndpointName",
            "type": "Attribute",
        },
    )
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
