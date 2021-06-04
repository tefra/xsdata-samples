from dataclasses import dataclass, field
from typing import List, Optional
from netex.models.dead_run_ref import DeadRunRef
from netex.models.journey_wait_time_versioned_child_structure import JourneyWaitTimeVersionedChildStructure
from netex.models.vehicle_journey_ref import VehicleJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleJourneyWaitTimeVersionedChildStructure(JourneyWaitTimeVersionedChildStructure):
    class Meta:
        name = "VehicleJourneyWaitTime_VersionedChildStructure"

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
