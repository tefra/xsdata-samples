from dataclasses import dataclass, field
from typing import List, Union
from .rendering import Rendering
from .t_implementation_value import TImplementationValue
from .t_task import TTask

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TUserTask(TTask):
    class Meta:
        name = "tUserTask"

    rendering: List[Rendering] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        }
    )
    implementation: Union[str, TImplementationValue] = field(
        default=TImplementationValue.UNSPECIFIED,
        metadata={
            "type": "Attribute",
        }
    )
