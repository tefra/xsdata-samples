from dataclasses import dataclass

from .validity_rule_parameter_ref_structure import (
    ValidityRuleParameterRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ValidityRuleParameterRef(ValidityRuleParameterRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
