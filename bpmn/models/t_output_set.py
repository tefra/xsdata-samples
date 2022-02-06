from dataclasses import dataclass, field
from typing import List, Optional
from .t_base_element import TBaseElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TOutputSet(TBaseElement):
    class Meta:
        name = "tOutputSet"

    data_output_refs: List[str] = field(
        default_factory=list,
        metadata={
            "name": "dataOutputRefs",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        }
    )
    optional_output_refs: List[str] = field(
        default_factory=list,
        metadata={
            "name": "optionalOutputRefs",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        }
    )
    while_executing_output_refs: List[str] = field(
        default_factory=list,
        metadata={
            "name": "whileExecutingOutputRefs",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        }
    )
    input_set_refs: List[str] = field(
        default_factory=list,
        metadata={
            "name": "inputSetRefs",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
