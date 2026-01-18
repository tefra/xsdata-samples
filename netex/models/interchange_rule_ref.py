from __future__ import annotations

from dataclasses import dataclass

from .interchange_rule_ref_structure import InterchangeRuleRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InterchangeRuleRef(InterchangeRuleRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
