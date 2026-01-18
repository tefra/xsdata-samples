from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LinkRefByValueStructure:
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
    from_point_ref: str = field(
        metadata={
            "name": "fromPointRef",
            "type": "Attribute",
            "required": True,
        }
    )
    to_point_ref: str = field(
        metadata={
            "name": "toPointRef",
            "type": "Attribute",
            "required": True,
        }
    )
    name_of_point_ref_class: None | str = field(
        default=None,
        metadata={
            "name": "nameOfPointRefClass",
            "type": "Attribute",
        },
    )
    type_of_link_ref: None | str = field(
        default=None,
        metadata={
            "name": "typeOfLinkRef",
            "type": "Attribute",
        },
    )
