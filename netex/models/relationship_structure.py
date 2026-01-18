from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RelationshipStructure:
    class Meta:
        name = "relationshipStructure"

    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
