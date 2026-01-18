from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .responsibility_set import ResponsibilitySet
from .responsibility_set_ref import ResponsibilitySetRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ResponsibilitySetsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "responsibilitySets_RelStructure"

    responsibility_set_ref_or_responsibility_set: Iterable[
        ResponsibilitySetRef | ResponsibilitySet
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ResponsibilitySetRef",
                    "type": ResponsibilitySetRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ResponsibilitySet",
                    "type": ResponsibilitySet,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
