from __future__ import annotations

from dataclasses import dataclass

from .vehicle_manoeuvring_requirement_ref_structure import (
    VehicleManoeuvringRequirementRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleManoeuvringRequirementRef(
    VehicleManoeuvringRequirementRefStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
