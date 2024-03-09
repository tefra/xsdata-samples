from dataclasses import dataclass, field
from typing import List, Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .type_of_usage_parameter import TypeOfUsageParameter
from .type_of_usage_parameter_ref import TypeOfUsageParameterRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfUsageParametersRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "typeOfUsageParameters_RelStructure"

    type_of_usage_parameter_ref_or_type_of_usage_parameter: List[
        Union[TypeOfUsageParameterRef, TypeOfUsageParameter]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TypeOfUsageParameterRef",
                    "type": TypeOfUsageParameterRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfUsageParameter",
                    "type": TypeOfUsageParameter,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
