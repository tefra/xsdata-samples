from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .service_facility_set import ServiceFacilitySet

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceFacilitySetsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "serviceFacilitySetsInFrame_RelStructure"

    service_facility_set: Sequence[ServiceFacilitySet] = field(
        default_factory=list,
        metadata={
            "name": "ServiceFacilitySet",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
