from __future__ import annotations

from dataclasses import dataclass

from .condition_summary_structure import ConditionSummaryStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ConditionSummary(ConditionSummaryStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
