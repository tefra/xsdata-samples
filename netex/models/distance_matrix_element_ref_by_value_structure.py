from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DistanceMatrixElementRefByValueStructure:
    name_of_class: None | str = field(
        default=None,
        metadata={
            "name": "nameOfClass",
            "type": "Attribute",
        },
    )
    created: None | XmlDateTime = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    changed: None | XmlDateTime = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    version: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    from_ref: None | str = field(
        default=None,
        metadata={
            "name": "fromRef",
            "type": "Attribute",
            "required": True,
        },
    )
    to_ref: None | str = field(
        default=None,
        metadata={
            "name": "toRef",
            "type": "Attribute",
            "required": True,
        },
    )
    name_of_point_ref_class: None | str = field(
        default=None,
        metadata={
            "name": "nameOfPointRefClass",
            "type": "Attribute",
        },
    )
