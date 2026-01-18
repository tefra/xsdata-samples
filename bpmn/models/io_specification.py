from __future__ import annotations

from dataclasses import dataclass

from .t_input_output_specification import TInputOutputSpecification

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class IoSpecification(TInputOutputSpecification):
    class Meta:
        name = "ioSpecification"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
