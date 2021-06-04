from dataclasses import dataclass
from netex.models.condition_summary_structure import ConditionSummaryStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ConditionSummary(ConditionSummaryStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
