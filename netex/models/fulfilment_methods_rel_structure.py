from dataclasses import dataclass, field
from typing import List, Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .fulfilment_method import FulfilmentMethod
from .fulfilment_method_ref import FulfilmentMethodRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FulfilmentMethodsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "fulfilmentMethods_RelStructure"

    fulfilment_method_ref_or_fulfilment_method: List[
        Union[FulfilmentMethodRef, FulfilmentMethod]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FulfilmentMethodRef",
                    "type": FulfilmentMethodRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FulfilmentMethod",
                    "type": FulfilmentMethod,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
