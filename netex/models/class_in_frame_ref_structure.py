from dataclasses import dataclass, field

from .class_ref_structure import ClassRefStructure
from .class_ref_type_enumeration import ClassRefTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ClassInFrameRefStructure(ClassRefStructure):
    class_ref_type: ClassRefTypeEnumeration = field(
        default=ClassRefTypeEnumeration.MEMBERS,
        metadata={
            "name": "classRefType",
            "type": "Attribute",
        },
    )
