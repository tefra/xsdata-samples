from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .service_facility_set import ServiceFacilitySet

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceFacilitySetsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "serviceFacilitySetsInFrame_RelStructure"

    service_facility_set: Iterable[ServiceFacilitySet] = field(
        default_factory=list,
        metadata={
            "name": "ServiceFacilitySet",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
