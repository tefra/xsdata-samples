from dataclasses import dataclass, field
from typing import Optional
from .onward_vehicle_meeting_link_ref import OnwardVehicleMeetingLinkRef
from .point_in_journey_pattern_versioned_child_structure import (
    PointInJourneyPatternVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleMeetingPointInPathVersionStructure(
    PointInJourneyPatternVersionedChildStructure
):
    class Meta:
        name = "VehicleMeetingPointInPath_VersionStructure"

    onward_vehicle_meeting_link_ref: Optional[
        OnwardVehicleMeetingLinkRef
    ] = field(
        default=None,
        metadata={
            "name": "OnwardVehicleMeetingLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
