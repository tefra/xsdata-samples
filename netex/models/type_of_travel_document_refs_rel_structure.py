from dataclasses import dataclass, field
from typing import List

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .type_of_travel_document_ref import TypeOfTravelDocumentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfTravelDocumentRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "TypeOfTravelDocumentRefs_RelStructure"

    type_of_travel_document_ref: List[TypeOfTravelDocumentRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfTravelDocumentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
