from __future__ import annotations

from dataclasses import dataclass

from .t_sequence_flow import TSequenceFlow

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class SequenceFlow(TSequenceFlow):
    class Meta:
        name = "sequenceFlow"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
