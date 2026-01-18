from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .train_number import TrainNumber
from .train_number_ref import TrainNumberRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainNumbersInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "trainNumbersInFrame_RelStructure"

    train_number_or_train_number_ref: Iterable[
        TrainNumber | TrainNumberRef
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TrainNumber",
                    "type": TrainNumber,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainNumberRef",
                    "type": TrainNumberRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
