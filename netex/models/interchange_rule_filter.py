from __future__ import annotations

from dataclasses import dataclass

from .interchange_rule_parameter_structure import (
    InterchangeRuleParameterStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InterchangeRuleFilter(InterchangeRuleParameterStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
