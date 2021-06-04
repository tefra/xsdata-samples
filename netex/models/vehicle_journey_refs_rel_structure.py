from dataclasses import dataclass, field
from typing import List
from netex.models.dead_run_ref import DeadRunRef
from netex.models.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.models.vehicle_journey_ref import VehicleJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleJourneyRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "vehicleJourneyRefs_RelStructure"

    dead_run_ref: List[DeadRunRef] = field(
        default_factory=list,
        metadata={
            "name": "DeadRunRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    vehicle_journey_ref: List[VehicleJourneyRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
