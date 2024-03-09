from dataclasses import dataclass, field
from typing import List, Union

from .car_model_profile import CarModelProfile
from .containment_aggregation_structure import ContainmentAggregationStructure
from .cycle_model_profile import CycleModelProfile

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleModelProfilesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "vehicleModelProfilesInFrame_RelStructure"

    car_model_profile_or_cycle_model_profile: List[
        Union[CarModelProfile, CycleModelProfile]
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
