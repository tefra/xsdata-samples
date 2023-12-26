from dataclasses import dataclass
from .facility_requirement_version_structure import (
    FacilityRequirementVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FacilityRequirement(FacilityRequirementVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
