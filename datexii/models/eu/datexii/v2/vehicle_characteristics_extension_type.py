from dataclasses import dataclass, field
from typing import List, Optional
from datexii.models.eu.datexii.v2.vehicle_characteristics_extended import (
    VehicleCharacteristicsExtended,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class VehicleCharacteristicsExtensionType:
    class Meta:
        name = "_VehicleCharacteristicsExtensionType"

    vehicle_characteristics_extended: Optional[
        VehicleCharacteristicsExtended
    ] = field(
        default=None,
        metadata={
            "name": "vehicleCharacteristicsExtended",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
