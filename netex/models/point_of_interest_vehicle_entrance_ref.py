from dataclasses import dataclass
from .point_of_interest_vehicle_entrance_ref_structure import (
    PointOfInterestVehicleEntranceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointOfInterestVehicleEntranceRef(
    PointOfInterestVehicleEntranceRefStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
