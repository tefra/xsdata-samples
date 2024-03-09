from dataclasses import dataclass, field
from typing import Optional

from .service_facility_sets_rel_structure import (
    ServiceFacilitySetsRelStructure,
)
from .vehicle_requirement_version_structure import (
    VehicleRequirementVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FacilityRequirementVersionStructure(VehicleRequirementVersionStructure):
    class Meta:
        name = "FacilityRequirement_VersionStructure"

    facility_sets: Optional[ServiceFacilitySetsRelStructure] = field(
        default=None,
        metadata={
            "name": "facilitySets",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
