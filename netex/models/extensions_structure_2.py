from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
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
