from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LinkRefByValueStructure:
    name_of_class: str | None = field(
        default=None,
        metadata={
            "name": "nameOfClass",
            "type": "Attribute",
        },
    )
    created: XmlDateTime | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    changed: XmlDateTime | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    version: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    from_point_ref: str | None = field(
        default=None,
        metadata={
            "name": "fromPointRef",
            "type": "Attribute",
            "required": True,
        },
    )
    to_point_ref: str | None = field(
        default=None,
        metadata={
            "name": "toPointRef",
            "type": "Attribute",
            "required": True,
        },
    )
    name_of_point_ref_class: str | None = field(
        default=None,
        metadata={
            "name": "nameOfPointRefClass",
            "type": "Attribute",
        },
    )
    type_of_link_ref: str | None = field(
        default=None,
        metadata={
            "name": "typeOfLinkRef",
            "type": "Attribute",
        },
    )
