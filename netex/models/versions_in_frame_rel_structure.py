from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .version import Version

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VersionsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "versionsInFrame_RelStructure"

    version: Iterable[Version] = field(
        default_factory=list,
        metadata={
            "name": "Version",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
