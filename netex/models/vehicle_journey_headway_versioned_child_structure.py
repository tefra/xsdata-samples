from dataclasses import dataclass, field
from typing import List
from .dead_run_ref import DeadRunRef
from .journey_headway_versioned_child_structure import JourneyHeadwayVersionedChildStructure
from .timing_point_in_journey_pattern_ref import TimingPointInJourneyPatternRef
from .vehicle_journey_ref import VehicleJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleJourneyHeadwayVersionedChildStructure(JourneyHeadwayVersionedChildStructure):
    class Meta:
        name = "VehicleJourneyHeadway_VersionedChildStructure"

    dead_run_ref_or_vehicle_journey_ref_or_timing_point_in_journey_pattern_ref: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DeadRunRef",
                    "type": DeadRunRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleJourneyRef",
                    "type": VehicleJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingPointInJourneyPatternRef",
                    "type": TimingPointInJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 2,
        }
    )
