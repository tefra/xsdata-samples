from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName

from .artifact import Artifact
from .association import Association
from .auditing import Auditing
from .boundary_event import BoundaryEvent
from .business_rule_task import BusinessRuleTask
from .call_activity import CallActivity
from .call_choreography import CallChoreography
from .choreography_task import ChoreographyTask
from .complex_gateway import ComplexGateway
from .correlation_subscription import CorrelationSubscription
from .data_object import DataObject
from .data_object_reference import DataObjectReference
from .data_store_reference import DataStoreReference
from .end_event import EndEvent
from .event import Event
from .event_based_gateway import EventBasedGateway
from .exclusive_gateway import ExclusiveGateway
from .flow_element import FlowElement
from .group import Group
from .human_performer import HumanPerformer
from .implicit_throw_event import ImplicitThrowEvent
from .inclusive_gateway import InclusiveGateway
from .intermediate_catch_event import IntermediateCatchEvent
from .intermediate_throw_event import IntermediateThrowEvent
from .lane_set import LaneSet
from .manual_task import ManualTask
from .monitoring import Monitoring
from .parallel_gateway import ParallelGateway
from .performer import Performer
from .potential_owner import PotentialOwner
from .property import Property
from .receive_task import ReceiveTask
from .resource_role import ResourceRole
from .script_task import ScriptTask
from .send_task import SendTask
from .sequence_flow import SequenceFlow
from .service_task import ServiceTask
from .start_event import StartEvent
from .t_callable_element import TCallableElement
from .t_process_type import TProcessType
from .t_sub_choreography import (
    AdHocSubProcess,
    SubChoreography,
    SubProcess,
    Transaction,
)
from .task import Task
from .text_annotation import TextAnnotation
from .user_task import UserTask

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TProcess(TCallableElement):
    class Meta:
        name = "tProcess"

    auditing: Auditing | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    monitoring: Monitoring | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    property: list[Property] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    lane_set: list[LaneSet] = field(
        default_factory=list,
        metadata={
            "name": "laneSet",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    user_task: list[UserTask] = field(
        default_factory=list,
        metadata={
            "name": "userTask",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    transaction: list[Transaction] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    task: list[Task] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    sub_process: list[SubProcess] = field(
        default_factory=list,
        metadata={
            "name": "subProcess",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    sub_choreography: list[SubChoreography] = field(
        default_factory=list,
        metadata={
            "name": "subChoreography",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    start_event: list[StartEvent] = field(
        default_factory=list,
        metadata={
            "name": "startEvent",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    service_task: list[ServiceTask] = field(
        default_factory=list,
        metadata={
            "name": "serviceTask",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    sequence_flow: list[SequenceFlow] = field(
        default_factory=list,
        metadata={
            "name": "sequenceFlow",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    send_task: list[SendTask] = field(
        default_factory=list,
        metadata={
            "name": "sendTask",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    script_task: list[ScriptTask] = field(
        default_factory=list,
        metadata={
            "name": "scriptTask",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    receive_task: list[ReceiveTask] = field(
        default_factory=list,
        metadata={
            "name": "receiveTask",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    parallel_gateway: list[ParallelGateway] = field(
        default_factory=list,
        metadata={
            "name": "parallelGateway",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    manual_task: list[ManualTask] = field(
        default_factory=list,
        metadata={
            "name": "manualTask",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    intermediate_throw_event: list[IntermediateThrowEvent] = field(
        default_factory=list,
        metadata={
            "name": "intermediateThrowEvent",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    intermediate_catch_event: list[IntermediateCatchEvent] = field(
        default_factory=list,
        metadata={
            "name": "intermediateCatchEvent",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    inclusive_gateway: list[InclusiveGateway] = field(
        default_factory=list,
        metadata={
            "name": "inclusiveGateway",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    implicit_throw_event: list[ImplicitThrowEvent] = field(
        default_factory=list,
        metadata={
            "name": "implicitThrowEvent",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    exclusive_gateway: list[ExclusiveGateway] = field(
        default_factory=list,
        metadata={
            "name": "exclusiveGateway",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    event_based_gateway: list[EventBasedGateway] = field(
        default_factory=list,
        metadata={
            "name": "eventBasedGateway",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    event: list[Event] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    end_event: list[EndEvent] = field(
        default_factory=list,
        metadata={
            "name": "endEvent",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    data_store_reference: list[DataStoreReference] = field(
        default_factory=list,
        metadata={
            "name": "dataStoreReference",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    data_object_reference: list[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "dataObjectReference",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    data_object: list[DataObject] = field(
        default_factory=list,
        metadata={
            "name": "dataObject",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    complex_gateway: list[ComplexGateway] = field(
        default_factory=list,
        metadata={
            "name": "complexGateway",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    choreography_task: list[ChoreographyTask] = field(
        default_factory=list,
        metadata={
            "name": "choreographyTask",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    call_choreography: list[CallChoreography] = field(
        default_factory=list,
        metadata={
            "name": "callChoreography",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    call_activity: list[CallActivity] = field(
        default_factory=list,
        metadata={
            "name": "callActivity",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    business_rule_task: list[BusinessRuleTask] = field(
        default_factory=list,
        metadata={
            "name": "businessRuleTask",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    boundary_event: list[BoundaryEvent] = field(
        default_factory=list,
        metadata={
            "name": "boundaryEvent",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    ad_hoc_sub_process: list[AdHocSubProcess] = field(
        default_factory=list,
        metadata={
            "name": "adHocSubProcess",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    flow_element: list[FlowElement] = field(
        default_factory=list,
        metadata={
            "name": "flowElement",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    text_annotation: list[TextAnnotation] = field(
        default_factory=list,
        metadata={
            "name": "textAnnotation",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    group: list[Group] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    association: list[Association] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    artifact: list[Artifact] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    potential_owner: list[PotentialOwner] = field(
        default_factory=list,
        metadata={
            "name": "potentialOwner",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    human_performer: list[HumanPerformer] = field(
        default_factory=list,
        metadata={
            "name": "humanPerformer",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    performer: list[Performer] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    resource_role: list[ResourceRole] = field(
        default_factory=list,
        metadata={
            "name": "resourceRole",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    correlation_subscription: list[CorrelationSubscription] = field(
        default_factory=list,
        metadata={
            "name": "correlationSubscription",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    supports: list[QName] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    process_type: TProcessType = field(
        default=TProcessType.NONE,
        metadata={
            "name": "processType",
            "type": "Attribute",
        },
    )
    is_closed: bool = field(
        default=False,
        metadata={
            "name": "isClosed",
            "type": "Attribute",
        },
    )
    is_executable: bool | None = field(
        default=None,
        metadata={
            "name": "isExecutable",
            "type": "Attribute",
        },
    )
    definitional_collaboration_ref: QName | None = field(
        default=None,
        metadata={
            "name": "definitionalCollaborationRef",
            "type": "Attribute",
        },
    )
