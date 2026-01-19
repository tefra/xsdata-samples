from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .whitelist_ref import WhitelistRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class WhitelistRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "whitelistRefs_RelStructure"

    whitelist_ref: Sequence[WhitelistRef] = field(
        default_factory=list,
        metadata={
            "name": "WhitelistRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
