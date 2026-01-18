from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DistanceMatrixElementRefByValueStructure:
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
    from_ref: str | None = field(
        default=None,
        metadata={
            "name": "fromRef",
            "type": "Attribute",
            "required": True,
        },
    )
    to_ref: str | None = field(
        default=None,
        metadata={
            "name": "toRef",
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
