from dataclasses import dataclass
from netex.models.error_condition_structure import ErrorConditionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ErrorCondition(ErrorConditionStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
