from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.relief_opportunity import ReliefOpportunity
from netex.models.relief_opportunity_ref import ReliefOpportunityRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ReliefOpportunitiesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "reliefOpportunities_RelStructure"

    relief_opportunity_ref: List[ReliefOpportunityRef] = field(
        default_factory=list,
        metadata={
            "name": "ReliefOpportunityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    relief_opportunity: List[ReliefOpportunity] = field(
        default_factory=list,
        metadata={
            "name": "ReliefOpportunity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
