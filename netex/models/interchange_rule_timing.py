from __future__ import annotations

from dataclasses import dataclass

from .interchange_rule_timing_version_structure import (
    InterchangeRuleTimingVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InterchangeRuleTiming(InterchangeRuleTimingVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
