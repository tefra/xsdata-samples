from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.dated_special_service_ref import DatedSpecialServiceRef
from netex.models.special_service import SpecialService
from netex.models.special_service_ref import SpecialServiceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SpecialServicesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "specialServices_RelStructure"

    dated_special_service_ref: List[DatedSpecialServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "DatedSpecialServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    special_service_ref: List[SpecialServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "SpecialServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    special_service: List[SpecialService] = field(
        default_factory=list,
        metadata={
            "name": "SpecialService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
