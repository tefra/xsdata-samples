from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from .vehicle_requirement_version_structure import (
    VehicleRequirementVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleManoeuvringRequirementVersionStructure(
    VehicleRequirementVersionStructure
):
    class Meta:
        name = "VehicleManoeuvringRequirement_VersionStructure"

    reversible: None | bool = field(
        default=None,
        metadata={
            "name": "Reversible",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_turning_circle: None | Decimal = field(
        default=None,
        metadata={
            "name": "MinimumTurningCircle",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_overtaking_width: None | Decimal = field(
        default=None,
        metadata={
            "name": "MinimumOvertakingWidth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_length: None | Decimal = field(
        default=None,
        metadata={
            "name": "MinimumLength",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
