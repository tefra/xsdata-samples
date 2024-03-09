from dataclasses import dataclass, field
from typing import Optional

from .capping_rule_ref import CappingRuleRef
from .fare_price_versioned_child_structure import (
    FarePriceVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CappingRulePriceVersionedChildStructure(
    FarePriceVersionedChildStructure
):
    class Meta:
        name = "CappingRulePrice_VersionedChildStructure"

    capping_rule_ref: Optional[CappingRuleRef] = field(
        default=None,
        metadata={
            "name": "CappingRuleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
