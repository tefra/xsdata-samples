from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .site_facility_set import SiteFacilitySet
from .site_facility_set_ref import SiteFacilitySetRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SiteFacilitySetsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "siteFacilitySets_RelStructure"

    site_facility_set_ref_or_site_facility_set: Iterable[
        SiteFacilitySetRef | SiteFacilitySet
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SiteFacilitySetRef",
                    "type": SiteFacilitySetRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteFacilitySet",
                    "type": SiteFacilitySet,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
