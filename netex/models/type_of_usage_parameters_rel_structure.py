from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .type_of_usage_parameter import TypeOfUsageParameter
from .type_of_usage_parameter_ref import TypeOfUsageParameterRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfUsageParametersRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "typeOfUsageParameters_RelStructure"

    type_of_usage_parameter_ref: List[TypeOfUsageParameterRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfUsageParameterRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_usage_parameter: List[TypeOfUsageParameter] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfUsageParameter",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
