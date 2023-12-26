from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from .vehicle_requirement_version_structure import (
    VehicleRequirementVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleManoeuvringRequirementVersionStructure(
    VehicleRequirementVersionStructure
):
    class Meta:
        name = "VehicleManoeuvringRequirement_VersionStructure"

    reversible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Reversible",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_turning_circle: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MinimumTurningCircle",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_overtaking_width: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MinimumOvertakingWidth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_length: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MinimumLength",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
