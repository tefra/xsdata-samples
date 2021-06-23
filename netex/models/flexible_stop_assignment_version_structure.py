from dataclasses import dataclass, field
from typing import Optional
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

    flexible_stop_place_ref: Optional[FlexibleStopPlaceRef] = field(
        default=None,
        metadata={
            "name": "FlexibleStopPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    hail_and_ride_area_ref: Optional[HailAndRideAreaRef] = field(
        default=None,
        metadata={
            "name": "HailAndRideAreaRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_area_ref: Optional[FlexibleAreaRef] = field(
        default=None,
        metadata={
            "name": "FlexibleAreaRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_quay_ref: Optional[FlexibleQuayRef] = field(
        default=None,
        metadata={
            "name": "FlexibleQuayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
