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

    service_facility_set_ref_or_service_facility_set: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ServiceFacilitySetRef",
                    "type": ServiceFacilitySetRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceFacilitySet",
                    "type": ServiceFacilitySet,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
