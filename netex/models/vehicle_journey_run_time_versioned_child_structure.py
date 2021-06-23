from dataclasses import dataclass, field
from typing import Optional
from .dead_run_ref import DeadRunRef
from .journey_run_time_versioned_child_structure import JourneyRunTimeVersionedChildStructure
from .vehicle_journey_ref import VehicleJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleJourneyRunTimeVersionedChildStructure(JourneyRunTimeVersionedChildStructure):
    class Meta:
        name = "VehicleJourneyRunTime_VersionedChildStructure"

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
