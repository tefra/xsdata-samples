from dataclasses import dataclass, field
from typing import List, Optional
from .type_of_infolink_enumeration import TypeOfInfolinkEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class InfoLinkStructure:
    value: Optional[str] = field(
        default=None
    )
    type_of_info_link: List[TypeOfInfolinkEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "typeOfInfoLink",
            "type": "Attribute",
            "tokens": True,
        }
    )
