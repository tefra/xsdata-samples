from dataclasses import dataclass, field
from typing import Optional
from netex.models.fare_class_enumeration import FareClassEnumeration
from netex.models.type_of_value_version_structure import TypeOfValueVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ClassOfUseValueStructure(TypeOfValueVersionStructure):
    class Meta:
        name = "ClassOfUse_ValueStructure"

    fare_class: Optional[FareClassEnumeration] = field(
        default=None,
        metadata={
            "name": "FareClass",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
