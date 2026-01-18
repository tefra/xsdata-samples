from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from .modification_enumeration import ModificationEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfVersionRefStructure:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    name_of_ref_class: str | None = field(
        default=None,
        metadata={
            "name": "nameOfRefClass",
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
    modification: ModificationEnumeration | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    ref: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version_ref: str | None = field(
        default=None,
        metadata={
            "name": "versionRef",
            "type": "Attribute",
        },
    )
