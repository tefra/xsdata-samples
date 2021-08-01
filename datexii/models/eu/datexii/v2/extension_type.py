from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ExtensionType:
    class Meta:
        name = "_ExtensionType"

    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )
