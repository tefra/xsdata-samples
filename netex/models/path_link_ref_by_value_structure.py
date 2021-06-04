from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PathLinkRefByValueStructure:
    name_of_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "nameOfClass",
            "type": "Attribute",
        }
    )
    created: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    changed: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    from_point_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "fromPointRef",
            "type": "Attribute",
            "required": True,
        }
    )
    to_point_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "toPointRef",
            "type": "Attribute",
            "required": True,
        }
    )
    name_of_point_ref_class: str = field(
        init=False,
        default="PathPoint",
        metadata={
            "name": "nameOfPointRefClass",
            "type": "Attribute",
        }
    )
    type_of_link_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "typeOfLinkRef",
            "type": "Attribute",
        }
    )
