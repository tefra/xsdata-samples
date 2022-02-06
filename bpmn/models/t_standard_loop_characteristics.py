from dataclasses import dataclass, field
from typing import Optional
from .t_expression import TExpression
from .t_loop_characteristics import TLoopCharacteristics

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TStandardLoopCharacteristics(TLoopCharacteristics):
    class Meta:
        name = "tStandardLoopCharacteristics"

    loop_condition: Optional[TExpression] = field(
        default=None,
        metadata={
            "name": "loopCondition",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        }
    )
    test_before: bool = field(
        default=False,
        metadata={
            "name": "testBefore",
            "type": "Attribute",
        }
    )
    loop_maximum: Optional[int] = field(
        default=None,
        metadata={
            "name": "loopMaximum",
            "type": "Attribute",
        }
    )
