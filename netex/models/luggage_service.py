from dataclasses import dataclass
from .luggage_service_version_structure import LuggageServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LuggageService(LuggageServiceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
