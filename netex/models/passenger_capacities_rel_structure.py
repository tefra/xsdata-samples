from dataclasses import dataclass, field
from typing import List
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .passenger_capacity import PassengerCapacity
from .passenger_capacity_ref import PassengerCapacityRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PassengerCapacitiesRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "passengerCapacities_RelStructure"

    passenger_capacity_ref: List[PassengerCapacityRef] = field(
        default_factory=list,
        metadata={
            "name": "PassengerCapacityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    passenger_capacity: List[PassengerCapacity] = field(
        default_factory=list,
        metadata={
            "name": "PassengerCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
