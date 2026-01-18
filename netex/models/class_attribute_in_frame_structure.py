from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

from .mandatory_enumeration import MandatoryEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ClassAttributeInFrameStructure:
    type_value: QName | None = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    mandatory: MandatoryEnumeration | None = field(
        default=None,
        metadata={
            "name": "Mandatory",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    name: QName | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
