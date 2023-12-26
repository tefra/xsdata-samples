from dataclasses import dataclass, field
from typing import Optional
from .t_event_definition import TEventDefinition
from .t_expression import TExpression

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TTimerEventDefinition(TEventDefinition):
    class Meta:
        name = "tTimerEventDefinition"

    time_date: Optional[TExpression] = field(
        default=None,
        metadata={
            "name": "timeDate",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    time_duration: Optional[TExpression] = field(
        default=None,
        metadata={
            "name": "timeDuration",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    time_cycle: Optional[TExpression] = field(
        default=None,
        metadata={
            "name": "timeCycle",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
