from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .flexible_area_ref import FlexibleAreaRef
from .flexible_quay import FlexibleQuay
from .flexible_quay_ref import FlexibleQuayRef
from .hail_and_ride_area_ref import HailAndRideAreaRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexibleQuaysRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "flexibleQuays_RelStructure"

    choice: Iterable[
        HailAndRideAreaRef | FlexibleAreaRef | FlexibleQuayRef | FlexibleQuay
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "HailAndRideAreaRef",
                    "type": HailAndRideAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleAreaRef",
                    "type": FlexibleAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleQuayRef",
                    "type": FlexibleQuayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleQuay",
                    "type": FlexibleQuay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
