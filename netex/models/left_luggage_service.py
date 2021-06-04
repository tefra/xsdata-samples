from dataclasses import dataclass
from netex.models.left_luggage_service_version_structure import LeftLuggageServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LeftLuggageService(LeftLuggageServiceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
