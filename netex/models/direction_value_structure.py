from dataclasses import dataclass, field
from typing import Optional

from .direction_ref_structure import DirectionRefStructure
from .direction_type import DirectionType
from .external_object_ref_structure import ExternalObjectRefStructure
from .type_of_value_version_structure import TypeOfValueVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DirectionValueStructure(TypeOfValueVersionStructure):
    class Meta:
        name = "Direction_ValueStructure"

    external_direction_ref: ExternalObjectRefStructure | None = field(
        default=None,
        metadata={
            "name": "ExternalDirectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    direction_type: DirectionType | None = field(
        default=None,
        metadata={
            "name": "DirectionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    opposite_direction_ref: DirectionRefStructure | None = field(
        default=None,
        metadata={
            "name": "OppositeDirectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
