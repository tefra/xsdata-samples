from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .group_of_timebands import GroupOfTimebands

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfTimebandsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "groupOfTimebandsInFrame_RelStructure"

    group_of_timebands: Sequence[GroupOfTimebands] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfTimebands",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
