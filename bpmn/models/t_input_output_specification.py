from dataclasses import dataclass, field
from typing import List
from .data_input import DataInput
from .data_output import DataOutput
from .input_set import InputSet
from .output_set import OutputSet
from .t_base_element import TBaseElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TInputOutputSpecification(TBaseElement):
    class Meta:
        name = "tInputOutputSpecification"

    data_input: List[DataInput] = field(
        default_factory=list,
        metadata={
            "name": "dataInput",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        }
    )
    data_output: List[DataOutput] = field(
        default_factory=list,
        metadata={
            "name": "dataOutput",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        }
    )
    input_set: List[InputSet] = field(
        default_factory=list,
        metadata={
            "name": "inputSet",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
            "min_occurs": 1,
        }
    )
    output_set: List[OutputSet] = field(
        default_factory=list,
        metadata={
            "name": "outputSet",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
            "min_occurs": 1,
        }
    )
