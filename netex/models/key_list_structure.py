from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .key_value_structure import KeyValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class KeyListStructure:
    key_value: Sequence[KeyValueStructure] = field(
        default_factory=list,
        metadata={
            "name": "KeyValue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
