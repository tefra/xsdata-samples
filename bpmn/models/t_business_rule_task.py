from __future__ import annotations

from dataclasses import dataclass, field

from .t_implementation_value import TImplementationValue
from .t_task import TTask

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class TBusinessRuleTask(TTask):
    class Meta:
        name = "tBusinessRuleTask"

    implementation: str | TImplementationValue = field(
        default=TImplementationValue.UNSPECIFIED,
        metadata={
            "type": "Attribute",
        },
    )
