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

    reversible: bool | None = field(
        default=None,
        metadata={
            "name": "Reversible",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_turning_circle: Decimal | None = field(
        default=None,
        metadata={
            "name": "MinimumTurningCircle",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_overtaking_width: Decimal | None = field(
        default=None,
        metadata={
            "name": "MinimumOvertakingWidth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_length: Decimal | None = field(
        default=None,
        metadata={
            "name": "MinimumLength",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
