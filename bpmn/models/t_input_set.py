from dataclasses import dataclass, field
from typing import List, Optional

from .t_base_element import TBaseElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TInputSet(TBaseElement):
    class Meta:
        name = "tInputSet"

    data_input_refs: List[str] = field(
        default_factory=list,
        metadata={
            "name": "dataInputRefs",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    optional_input_refs: List[str] = field(
        default_factory=list,
        metadata={
            "name": "optionalInputRefs",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    while_executing_input_refs: List[str] = field(
        default_factory=list,
        metadata={
            "name": "whileExecutingInputRefs",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    output_set_refs: List[str] = field(
        default_factory=list,
        metadata={
            "name": "outputSetRefs",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
