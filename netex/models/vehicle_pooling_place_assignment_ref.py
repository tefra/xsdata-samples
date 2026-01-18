from __future__ import annotations

from dataclasses import dataclass

from .vehicle_pooling_place_assignment_ref_structure import (
    VehiclePoolingPlaceAssignmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehiclePoolingPlaceAssignmentRef(
    VehiclePoolingPlaceAssignmentRefStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
