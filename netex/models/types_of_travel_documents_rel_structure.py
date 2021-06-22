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

    type_of_travel_document_ref_or_type_of_travel_document: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TypeOfTravelDocumentRef",
                    "type": TypeOfTravelDocumentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfTravelDocument",
                    "type": TypeOfTravelDocument,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
