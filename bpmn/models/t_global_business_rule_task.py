from dataclasses import dataclass, field
from typing import Union
from .t_global_task import TGlobalTask
from .t_implementation_value import TImplementationValue

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TGlobalBusinessRuleTask(TGlobalTask):
    class Meta:
        name = "tGlobalBusinessRuleTask"

    implementation: Union[str, TImplementationValue] = field(
        default=TImplementationValue.UNSPECIFIED,
        metadata={
            "type": "Attribute",
        },
    )
