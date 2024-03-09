from dataclasses import dataclass

from .validity_condition_ref_structure import ValidityConditionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ValidityRuleParameterRefStructure(ValidityConditionRefStructure):
    pass
