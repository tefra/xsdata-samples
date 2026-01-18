from __future__ import annotations

from dataclasses import dataclass, field

from .t_global_task import TGlobalTask
from .t_implementation_value import TImplementationValue

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class TGlobalBusinessRuleTask(TGlobalTask):
    class Meta:
        name = "tGlobalBusinessRuleTask"

    implementation: str | TImplementationValue = field(
        default=TImplementationValue.UNSPECIFIED,
        metadata={
            "type": "Attribute",
        },
    )
