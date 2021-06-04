from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.site_facility_set import SiteFacilitySet
from netex.models.site_facility_set_ref import SiteFacilitySetRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SiteFacilitySetsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "siteFacilitySets_RelStructure"

    site_facility_set_ref: List[SiteFacilitySetRef] = field(
        default_factory=list,
        metadata={
            "name": "SiteFacilitySetRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    site_facility_set: List[SiteFacilitySet] = field(
        default_factory=list,
        metadata={
            "name": "SiteFacilitySet",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
