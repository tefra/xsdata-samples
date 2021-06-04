from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from netex.models.modification_enumeration import ModificationEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SeatingEquipmentRefStructure:
    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    name_of_ref_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "nameOfRefClass",
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
    modification: Optional[ModificationEnumeration] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    version_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "versionRef",
            "type": "Attribute",
        }
    )
