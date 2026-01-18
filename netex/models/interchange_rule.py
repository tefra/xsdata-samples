from __future__ import annotations

from dataclasses import dataclass

from .interchange_rule_version_structure import InterchangeRuleVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class InterchangeRule(InterchangeRuleVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
