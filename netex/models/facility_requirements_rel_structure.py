from dataclasses import dataclass, field
from typing import List, Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .facility_requirement import FacilityRequirement
from .facility_requirement_ref import FacilityRequirementRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FacilityRequirementsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "facilityRequirements_RelStructure"

    facility_requirement_ref_or_facility_requirement: List[
        Union[FacilityRequirementRef, FacilityRequirement]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FacilityRequirementRef",
                    "type": FacilityRequirementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FacilityRequirement",
                    "type": FacilityRequirement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
