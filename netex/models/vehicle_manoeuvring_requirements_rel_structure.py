from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .vehicle_manoeuvring_requirement import VehicleManoeuvringRequirement
from .vehicle_manoeuvring_requirement_ref import (
    VehicleManoeuvringRequirementRef,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleManoeuvringRequirementsRelStructure(
    ContainmentAggregationStructure
):
    class Meta:
        name = "vehicleManoeuvringRequirements_RelStructure"

    vehicle_manoeuvring_requirement_ref_or_vehicle_manoeuvring_requirement: Iterable[
        Union[VehicleManoeuvringRequirementRef, VehicleManoeuvringRequirement]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehicleManoeuvringRequirementRef",
                    "type": VehicleManoeuvringRequirementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleManoeuvringRequirement",
                    "type": VehicleManoeuvringRequirement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
