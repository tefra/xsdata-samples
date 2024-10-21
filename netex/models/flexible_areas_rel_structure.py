from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .flexible_area import FlexibleArea
from .flexible_area_ref import FlexibleAreaRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FlexibleAreasRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "flexibleAreas_RelStructure"

    flexible_area_ref_or_flexible_area: Iterable[
        Union[FlexibleAreaRef, FlexibleArea]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FlexibleAreaRef",
                    "type": FlexibleAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleArea",
                    "type": FlexibleArea,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
