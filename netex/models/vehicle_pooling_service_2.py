from dataclasses import dataclass
from .mobility_service_version_structure import MobilityServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehiclePoolingService2(MobilityServiceVersionStructure):
    class Meta:
        name = "VehiclePoolingService_"
        namespace = "http://www.netex.org.uk/netex"
