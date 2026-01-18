from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .related_organisation import RelatedOrganisation

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RelatedOrganisationsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "relatedOrganisations_RelStructure"

    related_organisation: Iterable[RelatedOrganisation] = field(
        default_factory=list,
        metadata={
            "name": "RelatedOrganisation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
