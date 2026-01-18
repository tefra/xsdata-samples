from __future__ import annotations

from dataclasses import dataclass, field

from .service_facility_sets_rel_structure import (
    ServiceFacilitySetsRelStructure,
)
from .vehicle_requirement_version_structure import (
    VehicleRequirementVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FacilityRequirementVersionStructure(VehicleRequirementVersionStructure):
    class Meta:
        name = "FacilityRequirement_VersionStructure"

    facility_sets: None | ServiceFacilitySetsRelStructure = field(
        default=None,
        metadata={
            "name": "facilitySets",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
