from dataclasses import dataclass, field

from .route_ref import RouteRef
from .sections_in_sequence_rel_structure import LinkSequenceVersionStructure
from .vehicle_meeting_points_in_sequence_rel_structure import (
    VehicleMeetingPointsInSequenceRelStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SingleJourneyPathVersionStructure(LinkSequenceVersionStructure):
    class Meta:
        name = "SingleJourneyPath_VersionStructure"

    route_ref: RouteRef | None = field(
        default=None,
        metadata={
            "name": "RouteRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    points_in_sequence: VehicleMeetingPointsInSequenceRelStructure | None = (
        field(
            default=None,
            metadata={
                "name": "pointsInSequence",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
