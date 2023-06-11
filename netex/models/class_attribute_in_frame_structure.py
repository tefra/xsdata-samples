from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName
from .mandatory_enumeration import MandatoryEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ClassAttributeInFrameStructure:
    type_value: Optional[QName] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    mandatory: Optional[MandatoryEnumeration] = field(
        default=None,
        metadata={
            "name": "Mandatory",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    name: Optional[QName] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
