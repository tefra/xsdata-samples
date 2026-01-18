from dataclasses import dataclass, field

from .bpmndiagram import Bpmndiagram
from .cancel_event_definition import CancelEventDefinition
from .category import Category
from .choreography import Choreography
from .collaboration import Collaboration
from .compensate_event_definition import CompensateEventDefinition
from .conditional_event_definition import ConditionalEventDefinition
from .correlation_property import CorrelationProperty
from .data_store import DataStore
from .end_point import EndPoint
from .error import Error
from .error_event_definition import ErrorEventDefinition
from .escalation import Escalation
from .escalation_event_definition import EscalationEventDefinition
from .event_definition import EventDefinition
from .extension import Extension
from .global_business_rule_task import GlobalBusinessRuleTask
from .global_choreography_task import GlobalChoreographyTask
from .global_conversation import GlobalConversation
from .global_manual_task import GlobalManualTask
from .global_script_task import GlobalScriptTask
from .global_task import GlobalTask
from .global_user_task import GlobalUserTask
from .import_mod import Import
from .interface import Interface
from .item_definition import ItemDefinition
from .link_event_definition import LinkEventDefinition
from .message import Message
from .message_event_definition import MessageEventDefinition
from .partner_entity import PartnerEntity
from .partner_role import PartnerRole
from .process import Process
from .relationship import Relationship
from .resource import Resource
from .root_element import RootElement
from .signal import Signal
from .signal_event_definition import SignalEventDefinition
from .terminate_event_definition import TerminateEventDefinition
from .timer_event_definition import TimerEventDefinition

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TDefinitions:
    class Meta:
        name = "tDefinitions"

    import_value: list[Import] = field(
        default_factory=list,
        metadata={
            "name": "import",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    extension: list[Extension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    signal: list[Signal] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    resource: list[Resource] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    process: list[Process] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    partner_role: list[PartnerRole] = field(
        default_factory=list,
        metadata={
            "name": "partnerRole",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    partner_entity: list[PartnerEntity] = field(
        default_factory=list,
        metadata={
            "name": "partnerEntity",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    message: list[Message] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    item_definition: list[ItemDefinition] = field(
        default_factory=list,
        metadata={
            "name": "itemDefinition",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    interface: list[Interface] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    global_user_task: list[GlobalUserTask] = field(
        default_factory=list,
        metadata={
            "name": "globalUserTask",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    global_task: list[GlobalTask] = field(
        default_factory=list,
        metadata={
            "name": "globalTask",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    global_script_task: list[GlobalScriptTask] = field(
        default_factory=list,
        metadata={
            "name": "globalScriptTask",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    global_manual_task: list[GlobalManualTask] = field(
        default_factory=list,
        metadata={
            "name": "globalManualTask",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    global_business_rule_task: list[GlobalBusinessRuleTask] = field(
        default_factory=list,
        metadata={
            "name": "globalBusinessRuleTask",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    timer_event_definition: list[TimerEventDefinition] = field(
        default_factory=list,
        metadata={
            "name": "timerEventDefinition",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    terminate_event_definition: list[TerminateEventDefinition] = field(
        default_factory=list,
        metadata={
            "name": "terminateEventDefinition",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    signal_event_definition: list[SignalEventDefinition] = field(
        default_factory=list,
        metadata={
            "name": "signalEventDefinition",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    message_event_definition: list[MessageEventDefinition] = field(
        default_factory=list,
        metadata={
            "name": "messageEventDefinition",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    link_event_definition: list[LinkEventDefinition] = field(
        default_factory=list,
        metadata={
            "name": "linkEventDefinition",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    escalation_event_definition: list[EscalationEventDefinition] = field(
        default_factory=list,
        metadata={
            "name": "escalationEventDefinition",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    error_event_definition: list[ErrorEventDefinition] = field(
        default_factory=list,
        metadata={
            "name": "errorEventDefinition",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    conditional_event_definition: list[ConditionalEventDefinition] = field(
        default_factory=list,
        metadata={
            "name": "conditionalEventDefinition",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    compensate_event_definition: list[CompensateEventDefinition] = field(
        default_factory=list,
        metadata={
            "name": "compensateEventDefinition",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    cancel_event_definition: list[CancelEventDefinition] = field(
        default_factory=list,
        metadata={
            "name": "cancelEventDefinition",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    event_definition: list[EventDefinition] = field(
        default_factory=list,
        metadata={
            "name": "eventDefinition",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    escalation: list[Escalation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    error: list[Error] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    end_point: list[EndPoint] = field(
        default_factory=list,
        metadata={
            "name": "endPoint",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    data_store: list[DataStore] = field(
        default_factory=list,
        metadata={
            "name": "dataStore",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    correlation_property: list[CorrelationProperty] = field(
        default_factory=list,
        metadata={
            "name": "correlationProperty",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    global_conversation: list[GlobalConversation] = field(
        default_factory=list,
        metadata={
            "name": "globalConversation",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    global_choreography_task: list[GlobalChoreographyTask] = field(
        default_factory=list,
        metadata={
            "name": "globalChoreographyTask",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    choreography: list[Choreography] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    collaboration: list[Collaboration] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    category: list[Category] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    root_element: list[RootElement] = field(
        default_factory=list,
        metadata={
            "name": "rootElement",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    bpmndiagram: list[Bpmndiagram] = field(
        default_factory=list,
        metadata={
            "name": "BPMNDiagram",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/DI",
        },
    )
    relationship: list[Relationship] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    name: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    target_namespace: str | None = field(
        default=None,
        metadata={
            "name": "targetNamespace",
            "type": "Attribute",
            "required": True,
        },
    )
    expression_language: str = field(
        default="http://www.w3.org/1999/XPath",
        metadata={
            "name": "expressionLanguage",
            "type": "Attribute",
        },
    )
    type_language: str = field(
        default="http://www.w3.org/2001/XMLSchema",
        metadata={
            "name": "typeLanguage",
            "type": "Attribute",
        },
    )
    exporter: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    exporter_version: str | None = field(
        default=None,
        metadata={
            "name": "exporterVersion",
            "type": "Attribute",
        },
    )
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
