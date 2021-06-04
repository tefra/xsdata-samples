from dataclasses import dataclass
from netex.models.publication_request_structure import PublicationRequestStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PublicationRequest(PublicationRequestStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
