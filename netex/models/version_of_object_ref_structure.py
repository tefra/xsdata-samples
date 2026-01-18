from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from .modification_enumeration import ModificationEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VersionOfObjectRefStructure:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    name_of_ref_class: None | str = field(
        default=None,
        metadata={
            "name": "nameOfRefClass",
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
    modification: None | ModificationEnumeration = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    ref: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version_ref: None | str = field(
        default=None,
        metadata={
            "name": "versionRef",
            "type": "Attribute",
        },
    )
