from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ExtensionsStructure2:
    class Meta:
        name = "ExtensionsStructure"

    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )
