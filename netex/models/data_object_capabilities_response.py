from dataclasses import dataclass
from netex.models.data_object_capabilities_response_structure import DataObjectCapabilitiesResponseStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DataObjectCapabilitiesResponse(DataObjectCapabilitiesResponseStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
