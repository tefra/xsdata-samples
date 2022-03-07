from dataclasses import dataclass, field
from typing import Dict, Optional
from xml.etree.ElementTree import QName

__NAMESPACE__ = "http://www.w3.org/2006/02/addressing/wsdl"


@dataclass
class ServiceNameType:
    value: Optional[QName] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    endpoint_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndpointName",
            "type": "Attribute",
        }
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )
