from dataclasses import dataclass
from .vehicle_pooling_service_version_structure import (
    VehiclePoolingServiceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TaxiServiceVersionStructure(VehiclePoolingServiceVersionStructure):
    class Meta:
        name = "TaxiService_VersionStructure"
