from dataclasses import dataclass, field
from typing import List, Optional
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
    hail_and_ride_area_ref: List[HailAndRideAreaRef] = field(
        default_factory=list,
        metadata={
            "name": "HailAndRideAreaRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    flexible_area_ref: List[FlexibleAreaRef] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleAreaRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
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
