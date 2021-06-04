from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DistanceMatrixElementRefByValueStructure:
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
    from_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "fromRef",
            "type": "Attribute",
            "required": True,
        }
    )
    to_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "toRef",
            "type": "Attribute",
            "required": True,
        }
    )
    name_of_point_ref_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "nameOfPointRefClass",
            "type": "Attribute",
        }
    )
