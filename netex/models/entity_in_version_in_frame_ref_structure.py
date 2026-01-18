from dataclasses import dataclass, field

from .version_of_object_ref_structure import VersionOfObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class EntityInVersionInFrameRefStructure(VersionOfObjectRefStructure):
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
