from dataclasses import dataclass, field
from typing import List, Union
from .access_right_in_product_ref import AccessRightInProductRef
from .controllable_element_in_sequence_ref import (
    ControllableElementInSequenceRef,
)
from .fare_structure_element_in_sequence_ref import (
    FareStructureElementInSequenceRef,
)
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareElementInSequenceRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "fareElementInSequenceRefs_RelStructure"

    fare_element_in_sequence_ref: List[
        Union[
            ControllableElementInSequenceRef,
            FareStructureElementInSequenceRef,
            AccessRightInProductRef,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ControllableElementInSequenceRef",
                    "type": ControllableElementInSequenceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareStructureElementInSequenceRef",
                    "type": FareStructureElementInSequenceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessRightInProductRef",
                    "type": AccessRightInProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
