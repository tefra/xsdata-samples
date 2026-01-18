from dataclasses import dataclass, field
from typing import Optional

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
