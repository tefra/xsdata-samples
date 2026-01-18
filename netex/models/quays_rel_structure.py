from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .quay import Quay
from .quay_ref import QuayRef
from .taxi_stand_ref import TaxiStandRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class QuaysRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "quays_RelStructure"

    taxi_stand_ref_or_quay_ref_or_quay: Iterable[
        TaxiStandRef | QuayRef | Quay
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TaxiStandRef",
                    "type": TaxiStandRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QuayRef",
                    "type": QuayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Quay",
                    "type": Quay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
