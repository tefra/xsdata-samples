from dataclasses import dataclass, field
from typing import Optional, Union

from .flexible_area_ref import FlexibleAreaRef
from .flexible_quay_ref import FlexibleQuayRef
from .flexible_stop_place_ref import FlexibleStopPlaceRef
from .hail_and_ride_area_ref import HailAndRideAreaRef
from .stop_assignment_version_structure import StopAssignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FlexibleStopAssignmentVersionStructure(StopAssignmentVersionStructure):
    class Meta:
        name = "FlexibleStopAssignment_VersionStructure"

    flexible_stop_place_ref: FlexibleStopPlaceRef | None = field(
        default=None,
        metadata={
            "name": "FlexibleStopPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    flexible_quay_ref: HailAndRideAreaRef | FlexibleAreaRef | FlexibleQuayRef | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "HailAndRideAreaRef",
                    "type": HailAndRideAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleAreaRef",
                    "type": FlexibleAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleQuayRef",
                    "type": FlexibleQuayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
