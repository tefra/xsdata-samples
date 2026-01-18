from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .codespace import Codespace
from .containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CodespacesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "codespacesInFrame_RelStructure"

    codespace: Iterable[Codespace] = field(
        default_factory=list,
        metadata={
            "name": "Codespace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
