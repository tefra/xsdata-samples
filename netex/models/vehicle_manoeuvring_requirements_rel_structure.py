from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .vehicle_manoeuvring_requirement import VehicleManoeuvringRequirement
from .vehicle_manoeuvring_requirement_ref import (
    VehicleManoeuvringRequirementRef,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleManoeuvringRequirementsRelStructure(
    ContainmentAggregationStructure
):
    class Meta:
        name = "vehicleManoeuvringRequirements_RelStructure"

    vehicle_manoeuvring_requirement_ref_or_vehicle_manoeuvring_requirement: Sequence[
        VehicleManoeuvringRequirementRef | VehicleManoeuvringRequirement
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
