from dataclasses import dataclass, field
from typing import List, Optional
from .dead_run_ref import DeadRunRef
from .journey_run_time_versioned_child_structure import JourneyRunTimeVersionedChildStructure
from .vehicle_journey_ref import VehicleJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleJourneyRunTimeVersionedChildStructure(JourneyRunTimeVersionedChildStructure):
    class Meta:
        name = "VehicleJourneyRunTime_VersionedChildStructure"

    dead_run_ref: List[DeadRunRef] = field(
        default_factory=list,
        metadata={
            "name": "DeadRunRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
        }
    )
    vehicle_journey_ref: Optional[VehicleJourneyRef] = field(
        default=None,
        metadata={
            "name": "VehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
