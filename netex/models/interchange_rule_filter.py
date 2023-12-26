from dataclasses import dataclass
from .interchange_rule_parameter_structure import (
    InterchangeRuleParameterStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class InterchangeRuleFilter(InterchangeRuleParameterStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
