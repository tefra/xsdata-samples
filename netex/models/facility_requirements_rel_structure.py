from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.facility_requirement import FacilityRequirement
from netex.models.facility_requirement_ref import FacilityRequirementRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FacilityRequirementsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "facilityRequirements_RelStructure"

    facility_requirement_ref: List[FacilityRequirementRef] = field(
        default_factory=list,
        metadata={
            "name": "FacilityRequirementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    facility_requirement: List[FacilityRequirement] = field(
        default_factory=list,
        metadata={
            "name": "FacilityRequirement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
