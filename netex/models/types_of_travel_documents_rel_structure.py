from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .type_of_travel_document import TypeOfTravelDocument
from .type_of_travel_document_ref import TypeOfTravelDocumentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypesOfTravelDocumentsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "typesOfTravelDocuments_RelStructure"

    type_of_travel_document_ref: List[TypeOfTravelDocumentRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfTravelDocumentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_travel_document: List[TypeOfTravelDocument] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfTravelDocument",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
