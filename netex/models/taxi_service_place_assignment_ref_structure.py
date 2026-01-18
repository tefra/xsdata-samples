from __future__ import annotations

from dataclasses import dataclass

from .vehicle_service_place_assignment_ref_structure import (
    VehicleServicePlaceAssignmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TaxiServicePlaceAssignmentRefStructure(
    VehicleServicePlaceAssignmentRefStructure
):
    pass
