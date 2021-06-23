from dataclasses import dataclass, field
from typing import Optional
from .dead_run_ref import DeadRunRef
from .journey_wait_time_versioned_child_structure import JourneyWaitTimeVersionedChildStructure
from .vehicle_journey_ref import VehicleJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleJourneyWaitTimeVersionedChildStructure(JourneyWaitTimeVersionedChildStructure):
    class Meta:
        name = "VehicleJourneyWaitTime_VersionedChildStructure"

    dead_run_ref: Optional[DeadRunRef] = field(
        default=None,
        metadata={
            "name": "DeadRunRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
