from dataclasses import dataclass
from .capping_rule_versioned_child_structure import (
    CappingRuleVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CappingRule(CappingRuleVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
