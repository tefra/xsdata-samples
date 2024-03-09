from dataclasses import dataclass, field
from typing import List, Optional
from xml.etree.ElementTree import QName

from .cancel_event_definition import CancelEventDefinition
from .compensate_event_definition import CompensateEventDefinition
from .conditional_event_definition import ConditionalEventDefinition
from .data_output import DataOutput
from .data_output_association import DataOutputAssociation
from .error_event_definition import ErrorEventDefinition
from .escalation_event_definition import EscalationEventDefinition
from .event_definition import EventDefinition
from .link_event_definition import LinkEventDefinition
from .message_event_definition import MessageEventDefinition
from .output_set import OutputSet
from .signal_event_definition import SignalEventDefinition
from .t_event import TEvent
from .terminate_event_definition import TerminateEventDefinition
from .timer_event_definition import TimerEventDefinition

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TCatchEvent(TEvent):
    class Meta:
        name = "tCatchEvent"

    data_output: List[DataOutput] = field(
        default_factory=list,
        metadata={
            "name": "dataOutput",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    data_output_association: List[DataOutputAssociation] = field(
        default_factory=list,
        metadata={
            "name": "dataOutputAssociation",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    output_set: Optional[OutputSet] = field(
        default=None,
        metadata={
            "name": "outputSet",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    timer_event_definition: List[TimerEventDefinition] = field(
        default_factory=list,
        metadata={
            "name": "timerEventDefinition",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    terminate_event_definition: List[TerminateEventDefinition] = field(
        default_factory=list,
        metadata={
            "name": "terminateEventDefinition",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    signal_event_definition: List[SignalEventDefinition] = field(
        default_factory=list,
        metadata={
            "name": "signalEventDefinition",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    message_event_definition: List[MessageEventDefinition] = field(
        default_factory=list,
        metadata={
            "name": "messageEventDefinition",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    link_event_definition: List[LinkEventDefinition] = field(
        default_factory=list,
        metadata={
            "name": "linkEventDefinition",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    escalation_event_definition: List[EscalationEventDefinition] = field(
        default_factory=list,
        metadata={
            "name": "escalationEventDefinition",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    error_event_definition: List[ErrorEventDefinition] = field(
        default_factory=list,
        metadata={
            "name": "errorEventDefinition",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    conditional_event_definition: List[ConditionalEventDefinition] = field(
        default_factory=list,
        metadata={
            "name": "conditionalEventDefinition",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    compensate_event_definition: List[CompensateEventDefinition] = field(
        default_factory=list,
        metadata={
            "name": "compensateEventDefinition",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    cancel_event_definition: List[CancelEventDefinition] = field(
        default_factory=list,
        metadata={
            "name": "cancelEventDefinition",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    event_definition: List[EventDefinition] = field(
        default_factory=list,
        metadata={
            "name": "eventDefinition",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    event_definition_ref: List[QName] = field(
        default_factory=list,
        metadata={
            "name": "eventDefinitionRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    parallel_multiple: bool = field(
        default=False,
        metadata={
            "name": "parallelMultiple",
            "type": "Attribute",
        },
    )
