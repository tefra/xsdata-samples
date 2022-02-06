from dataclasses import dataclass, field
from typing import Union
from .t_implementation_value import TImplementationValue
from .t_task import TTask

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TBusinessRuleTask(TTask):
    class Meta:
        name = "tBusinessRuleTask"

    implementation: Union[str, TImplementationValue] = field(
        default=TImplementationValue.UNSPECIFIED,
        metadata={
            "type": "Attribute",
        }
    )
