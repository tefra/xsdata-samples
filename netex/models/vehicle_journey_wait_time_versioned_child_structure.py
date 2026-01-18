from __future__ import annotations

from dataclasses import dataclass, field

from .dead_run_ref import DeadRunRef
from .journey_wait_time_versioned_child_structure import (
    JourneyWaitTimeVersionedChildStructure,
)
from .vehicle_journey_ref import VehicleJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleJourneyWaitTimeVersionedChildStructure(
    JourneyWaitTimeVersionedChildStructure
):
    class Meta:
        name = "VehicleJourneyWaitTime_VersionedChildStructure"

    vehicle_journey_ref: DeadRunRef | VehicleJourneyRef | None = field(
        default=None,
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
            ),
        },
    )
