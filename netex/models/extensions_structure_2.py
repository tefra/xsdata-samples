from collections.abc import Iterable
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ExtensionsStructure2:
    class Meta:
        name = "ExtensionsStructure"

    any_element: Iterable[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
