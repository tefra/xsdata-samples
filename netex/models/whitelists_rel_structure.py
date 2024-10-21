from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .whitelist import Whitelist
from .whitelist_ref import WhitelistRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class WhitelistsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "whitelists_RelStructure"

    whitelist_ref_or_whitelist: Iterable[Union[WhitelistRef, Whitelist]] = (
        field(
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
                        "name": "Whitelist",
                        "type": Whitelist,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                ),
            },
        )
    )
