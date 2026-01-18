from __future__ import annotations

from dataclasses import dataclass, field

from .t_base_element import TBaseElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class TInputSet(TBaseElement):
    class Meta:
        name = "tInputSet"

    data_input_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "dataInputRefs",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    optional_input_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "optionalInputRefs",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    while_executing_input_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "whileExecutingInputRefs",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    output_set_refs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "outputSetRefs",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
