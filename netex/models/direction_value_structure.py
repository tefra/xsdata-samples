from dataclasses import dataclass, field
from typing import Optional
from netex.models.direction_ref_structure import DirectionRefStructure
from netex.models.direction_type_enumeration import DirectionTypeEnumeration
from netex.models.external_object_ref_structure import ExternalObjectRefStructure
from netex.models.type_of_value_version_structure import TypeOfValueVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DirectionValueStructure(TypeOfValueVersionStructure):
    class Meta:
        name = "Direction_ValueStructure"

    external_direction_ref: Optional[ExternalObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "ExternalDirectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    direction_type: Optional[DirectionTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "DirectionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    opposite_direction_ref: Optional[DirectionRefStructure] = field(
        default=None,
        metadata={
            "name": "OppositeDirectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
