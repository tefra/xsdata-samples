from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .dead_run_ref import DeadRunRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .vehicle_journey_ref import VehicleJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleJourneyRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "vehicleJourneyRefs_RelStructure"

    vehicle_journey_ref: Iterable[DeadRunRef | VehicleJourneyRef] = (
        field(
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
                ),
            },
        )
    )
