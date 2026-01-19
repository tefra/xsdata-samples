from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .online_service_ref import OnlineServiceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OnlineServiceRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "onlineServiceRefs_RelStructure"

    online_service_ref: Sequence[OnlineServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "OnlineServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
