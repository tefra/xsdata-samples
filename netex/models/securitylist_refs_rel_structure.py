from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .blacklist_ref import BlacklistRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .whitelist_ref import WhitelistRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SecuritylistRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "securitylistRefs_RelStructure"

    security_list_ref: Sequence[WhitelistRef | BlacklistRef] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "WhitelistRef",
                    "type": WhitelistRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BlacklistRef",
                    "type": BlacklistRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
