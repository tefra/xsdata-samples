from __future__ import annotations

from dataclasses import dataclass

from .error_condition_structure import ErrorConditionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ErrorCondition(ErrorConditionStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
