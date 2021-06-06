from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from .modification_enumeration import ModificationEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AllOrganisationsRefStructure:
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
    ref: str = field(
        init=False,
        default="All",
        metadata={
            "type": "Attribute",
        }
    )
    version_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "versionRef",
            "type": "Attribute",
        }
    )
