from dataclasses import dataclass

from .vehicle_pooling_service_ref_structure import (
    VehiclePoolingServiceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TaxiServiceRefStructure(VehiclePoolingServiceRefStructure):
    pass
