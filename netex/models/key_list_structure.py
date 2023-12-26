from dataclasses import dataclass, field
from typing import List
from .key_value_structure import KeyValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class KeyListStructure:
    key_value: List[KeyValueStructure] = field(
        default_factory=list,
        metadata={
            "name": "KeyValue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
