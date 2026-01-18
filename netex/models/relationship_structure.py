from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RelationshipStructure:
    class Meta:
        name = "relationshipStructure"

    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
