from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .delta import Delta

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeltasRelStructure:
    class Meta:
        name = "deltas_RelStructure"

    delta: Iterable[Delta] = field(
        default_factory=list,
        metadata={
            "name": "Delta",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
