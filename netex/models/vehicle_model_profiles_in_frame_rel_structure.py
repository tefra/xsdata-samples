from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .car_model_profile import CarModelProfile
from .containment_aggregation_structure import ContainmentAggregationStructure
from .cycle_model_profile import CycleModelProfile

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleModelProfilesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "vehicleModelProfilesInFrame_RelStructure"

    car_model_profile_or_cycle_model_profile: Sequence[
        CarModelProfile | CycleModelProfile
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CarModelProfile",
                    "type": CarModelProfile,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CycleModelProfile",
                    "type": CycleModelProfile,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
