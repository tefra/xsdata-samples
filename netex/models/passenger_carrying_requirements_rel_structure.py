from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .passenger_carrying_requirement import PassengerCarryingRequirement
from .passenger_carrying_requirement_ref import PassengerCarryingRequirementRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PassengerCarryingRequirementsRelStructure(
    ContainmentAggregationStructure
):
    class Meta:
        name = "passengerCarryingRequirements_RelStructure"

    passenger_carrying_requirement_ref_or_passenger_carrying_requirement: Iterable[
        PassengerCarryingRequirementRef | PassengerCarryingRequirement
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PassengerCarryingRequirementRef",
                    "type": PassengerCarryingRequirementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerCarryingRequirement",
                    "type": PassengerCarryingRequirement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
