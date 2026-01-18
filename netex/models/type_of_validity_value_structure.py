from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

from .class_refs_rel_structure import ClassRefsRelStructure
from .frame_nature_enumeration import FrameNatureEnumeration
from .type_of_value_version_structure import TypeOfValueVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfValidityValueStructure(TypeOfValueVersionStructure):
    class Meta:
        name = "TypeOfValidity_ValueStructure"

    periodicity: XmlDuration | None = field(
        default=None,
        metadata={
            "name": "Periodicity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    nature: FrameNatureEnumeration | None = field(
        default=None,
        metadata={
            "name": "Nature",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    classes: ClassRefsRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
