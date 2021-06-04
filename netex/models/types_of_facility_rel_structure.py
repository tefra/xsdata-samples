from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.type_of_facility import TypeOfFacility
from netex.models.type_of_facility_ref import TypeOfFacilityRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypesOfFacilityRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "typesOfFacility_RelStructure"

    type_of_facility_ref: List[TypeOfFacilityRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFacilityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_facility: List[TypeOfFacility] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFacility",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
