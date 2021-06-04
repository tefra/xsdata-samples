from dataclasses import dataclass
from netex.models.type_of_travel_document_ref_structure import TypeOfTravelDocumentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfTravelDocumentRef(TypeOfTravelDocumentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
