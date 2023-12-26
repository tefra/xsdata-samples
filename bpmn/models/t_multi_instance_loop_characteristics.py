from dataclasses import dataclass, field
from typing import List, Optional
from xml.etree.ElementTree import QName
from .complex_behavior_definition import ComplexBehaviorDefinition
from .t_data_input import TDataInput
from .t_data_output import TDataOutput
from .t_expression import TExpression
from .t_loop_characteristics import TLoopCharacteristics
from .t_multi_instance_flow_condition import TMultiInstanceFlowCondition

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TMultiInstanceLoopCharacteristics(TLoopCharacteristics):
    class Meta:
        name = "tMultiInstanceLoopCharacteristics"

    loop_cardinality: Optional[TExpression] = field(
        default=None,
        metadata={
            "name": "loopCardinality",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    loop_data_input_ref: Optional[QName] = field(
        default=None,
        metadata={
            "name": "loopDataInputRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    loop_data_output_ref: Optional[QName] = field(
        default=None,
        metadata={
            "name": "loopDataOutputRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    input_data_item: Optional[TDataInput] = field(
        default=None,
        metadata={
            "name": "inputDataItem",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    output_data_item: Optional[TDataOutput] = field(
        default=None,
        metadata={
            "name": "outputDataItem",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    complex_behavior_definition: List[ComplexBehaviorDefinition] = field(
        default_factory=list,
        metadata={
            "name": "complexBehaviorDefinition",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    completion_condition: Optional[TExpression] = field(
        default=None,
        metadata={
            "name": "completionCondition",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    is_sequential: bool = field(
        default=False,
        metadata={
            "name": "isSequential",
            "type": "Attribute",
        },
    )
    behavior: TMultiInstanceFlowCondition = field(
        default=TMultiInstanceFlowCondition.ALL,
        metadata={
            "type": "Attribute",
        },
    )
    one_behavior_event_ref: Optional[QName] = field(
        default=None,
        metadata={
            "name": "oneBehaviorEventRef",
            "type": "Attribute",
        },
    )
    none_behavior_event_ref: Optional[QName] = field(
        default=None,
        metadata={
            "name": "noneBehaviorEventRef",
            "type": "Attribute",
        },
    )
