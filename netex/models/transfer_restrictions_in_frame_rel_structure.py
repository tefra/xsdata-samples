from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .transfer_restriction import TransferRestriction

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TransferRestrictionsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "transferRestrictionsInFrame_RelStructure"

    transfer_restriction: Sequence[TransferRestriction] = field(
        default_factory=list,
        metadata={
            "name": "TransferRestriction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
