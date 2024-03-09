from dataclasses import dataclass

from .left_luggage_service_ref_structure import LeftLuggageServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LeftLuggageServiceRef(LeftLuggageServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
