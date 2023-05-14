from dataclasses import dataclass, field
from typing import Optional
from .dead_run_ref import DeadRunRef
from .journey_layover_structure import JourneyLayoverStructure
from .vehicle_journey_ref import VehicleJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleJourneyLayoverVersionedChildStructure(JourneyLayoverStructure):
    class Meta:
        name = "VehicleJourneyLayover_VersionedChildStructure"

    dead_run_ref_or_vehicle_journey_ref: Optional[object] = field(
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
        }
    )
