from dataclasses import dataclass
from netex.models.type_of_travel_document_version_structure import TypeOfTravelDocumentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfTravelDocument(TypeOfTravelDocumentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
