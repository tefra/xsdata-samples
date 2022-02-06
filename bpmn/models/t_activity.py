from dataclasses import dataclass, field
from typing import List, Optional
from .data_input_association import DataInputAssociation
from .data_output_association import DataOutputAssociation
from .human_performer import HumanPerformer
from .io_specification import IoSpecification
from .loop_characteristics import LoopCharacteristics
from .multi_instance_loop_characteristics import MultiInstanceLoopCharacteristics
from .performer import Performer
from .potential_owner import PotentialOwner
from .property import Property
from .resource_role import ResourceRole
from .standard_loop_characteristics import StandardLoopCharacteristics
from .t_flow_node import TFlowNode

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TActivity(TFlowNode):
    class Meta:
        name = "tActivity"

    io_specification: Optional[IoSpecification] = field(
        default=None,
        metadata={
            "name": "ioSpecification",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        }
    )
    property: List[Property] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        }
    )
    data_input_association: List[DataInputAssociation] = field(
        default_factory=list,
        metadata={
            "name": "dataInputAssociation",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        }
    )
    data_output_association: List[DataOutputAssociation] = field(
        default_factory=list,
        metadata={
            "name": "dataOutputAssociation",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        }
    )
    potential_owner: List[PotentialOwner] = field(
        default_factory=list,
        metadata={
            "name": "potentialOwner",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        }
    )
    human_performer: List[HumanPerformer] = field(
        default_factory=list,
        metadata={
            "name": "humanPerformer",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        }
    )
    performer: List[Performer] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        }
    )
    resource_role: List[ResourceRole] = field(
        default_factory=list,
        metadata={
            "name": "resourceRole",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        }
    )
    standard_loop_characteristics: Optional[StandardLoopCharacteristics] = field(
        default=None,
        metadata={
            "name": "standardLoopCharacteristics",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        }
    )
    multi_instance_loop_characteristics: Optional[MultiInstanceLoopCharacteristics] = field(
        default=None,
        metadata={
            "name": "multiInstanceLoopCharacteristics",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        }
    )
    loop_characteristics: Optional[LoopCharacteristics] = field(
        default=None,
        metadata={
            "name": "loopCharacteristics",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        }
    )
    is_for_compensation: bool = field(
        default=False,
        metadata={
            "name": "isForCompensation",
            "type": "Attribute",
        }
    )
    start_quantity: int = field(
        default=1,
        metadata={
            "name": "startQuantity",
            "type": "Attribute",
        }
    )
    completion_quantity: int = field(
        default=1,
        metadata={
            "name": "completionQuantity",
            "type": "Attribute",
        }
    )
    default: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
