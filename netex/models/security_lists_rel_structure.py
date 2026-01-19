from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .blacklist_ref import BlacklistRef
from .containment_aggregation_structure import ContainmentAggregationStructure
from .whitelist_ref import WhitelistRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SecurityListsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "securityLists_RelStructure"

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
