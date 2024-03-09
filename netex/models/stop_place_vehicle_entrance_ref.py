from dataclasses import dataclass

from .stop_place_vehicle_entrance_ref_structure import (
    StopPlaceVehicleEntranceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StopPlaceVehicleEntranceRef(StopPlaceVehicleEntranceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
