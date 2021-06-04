from dataclasses import dataclass
from netex.models.data_object_service_capabilities_structure import DataObjectServiceCapabilitiesStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DataObjectServiceCapabilities(DataObjectServiceCapabilitiesStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
