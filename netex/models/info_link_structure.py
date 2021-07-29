from dataclasses import dataclass, field
from typing import List
from .type_of_infolink_enumeration import TypeOfInfolinkEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class InfoLinkStructure:
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    type_of_info_link: List[TypeOfInfolinkEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "typeOfInfoLink",
            "type": "Attribute",
            "tokens": True,
        }
    )
