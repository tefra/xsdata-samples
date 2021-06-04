from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.type_of_security_list import TypeOfSecurityList
from netex.models.type_of_security_list_ref import TypeOfSecurityListRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypesOfSecurityListRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "typesOfSecurityList_RelStructure"

    type_of_security_list_ref: List[TypeOfSecurityListRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfSecurityListRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_security_list: List[TypeOfSecurityList] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfSecurityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
