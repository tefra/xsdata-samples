from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .passenger_carrying_requirement import PassengerCarryingRequirement
from .passenger_carrying_requirement_ref import PassengerCarryingRequirementRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PassengerCarryingRequirementsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "passengerCarryingRequirements_RelStructure"

    passenger_carrying_requirement_ref: List[PassengerCarryingRequirementRef] = field(
        default_factory=list,
        metadata={
            "name": "PassengerCarryingRequirementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    passenger_carrying_requirement: List[PassengerCarryingRequirement] = field(
        default_factory=list,
        metadata={
            "name": "PassengerCarryingRequirement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
