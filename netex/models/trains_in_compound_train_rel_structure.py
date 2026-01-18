from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)
from .train_in_compound_train_versioned_child_structure import (
    TrainInCompoundTrainVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainsInCompoundTrainRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "trainsInCompoundTrain_RelStructure"

    train_in_compound_train: Iterable[
        TrainInCompoundTrainVersionedChildStructure
    ] = field(
        default_factory=list,
        metadata={
            "name": "TrainInCompoundTrain",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
