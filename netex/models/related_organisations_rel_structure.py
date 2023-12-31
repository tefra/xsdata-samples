from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .related_organisation import RelatedOrganisation

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RelatedOrganisationsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "relatedOrganisations_RelStructure"

    related_organisation: List[RelatedOrganisation] = field(
        default_factory=list,
        metadata={
            "name": "RelatedOrganisation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
