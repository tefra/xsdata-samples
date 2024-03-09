from dataclasses import dataclass

from .vehicle_rental_service_ref_structure import (
    VehicleRentalServiceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleRentalServiceRef(VehicleRentalServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
