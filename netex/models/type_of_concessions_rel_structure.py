from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .type_of_concession import TypeOfConcession
from .type_of_concession_ref import TypeOfConcessionRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfConcessionsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "typeOfConcessions_RelStructure"

    type_of_concession_ref: List[TypeOfConcessionRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfConcessionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_concession: List[TypeOfConcession] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfConcession",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
