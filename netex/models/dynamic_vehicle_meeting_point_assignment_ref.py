from __future__ import annotations

from dataclasses import dataclass

from .dynamic_vehicle_meeting_point_assignment_ref_structure import (
    DynamicVehicleMeetingPointAssignmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DynamicVehicleMeetingPointAssignmentRef(
    DynamicVehicleMeetingPointAssignmentRefStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
