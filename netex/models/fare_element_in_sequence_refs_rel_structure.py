from dataclasses import dataclass, field
from typing import List
from .access_right_in_product_ref import AccessRightInProductRef
from .controllable_element_in_sequence_ref import ControllableElementInSequenceRef
from .fare_element_in_sequence_ref import FareElementInSequenceRef
from .fare_structure_element_in_sequence_ref import FareStructureElementInSequenceRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareElementInSequenceRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "fareElementInSequenceRefs_RelStructure"

    controllable_element_in_sequence_ref: List[ControllableElementInSequenceRef] = field(
        default_factory=list,
        metadata={
            "name": "ControllableElementInSequenceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    fare_structure_element_in_sequence_ref: List[FareStructureElementInSequenceRef] = field(
        default_factory=list,
        metadata={
            "name": "FareStructureElementInSequenceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    access_right_in_product_ref: List[AccessRightInProductRef] = field(
        default_factory=list,
        metadata={
            "name": "AccessRightInProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    fare_element_in_sequence_ref: List[FareElementInSequenceRef] = field(
        default_factory=list,
        metadata={
            "name": "FareElementInSequenceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
