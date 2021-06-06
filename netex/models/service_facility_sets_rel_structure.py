from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .service_facility_set import ServiceFacilitySet
from .service_facility_set_ref import ServiceFacilitySetRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceFacilitySetsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "serviceFacilitySets_RelStructure"

    service_facility_set_ref: List[ServiceFacilitySetRef] = field(
        default_factory=list,
        metadata={
            "name": "ServiceFacilitySetRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_facility_set: List[ServiceFacilitySet] = field(
        default_factory=list,
        metadata={
            "name": "ServiceFacilitySet",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
