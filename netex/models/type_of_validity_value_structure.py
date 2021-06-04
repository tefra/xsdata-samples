from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from netex.models.class_refs_rel_structure import ClassRefsRelStructure
from netex.models.frame_nature_enumeration import FrameNatureEnumeration
from netex.models.type_of_value_version_structure import TypeOfValueVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfValidityValueStructure(TypeOfValueVersionStructure):
    class Meta:
        name = "TypeOfValidity_ValueStructure"

    periodicity: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "Periodicity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    nature: Optional[FrameNatureEnumeration] = field(
        default=None,
        metadata={
            "name": "Nature",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    classes: Optional[ClassRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
