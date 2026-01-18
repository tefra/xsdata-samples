from __future__ import annotations

from dataclasses import dataclass

from .limiting_rule_versioned_structure import LimitingRuleVersionedStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LimitingRule(LimitingRuleVersionedStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
