from __future__ import annotations

from dataclasses import dataclass, field

from .version_of_object_ref_structure import VersionOfObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EntityInVersionInFrameRefStructure(VersionOfObjectRefStructure):
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
