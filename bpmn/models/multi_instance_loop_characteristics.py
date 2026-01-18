from __future__ import annotations

from dataclasses import dataclass

from .t_multi_instance_loop_characteristics import (
    TMultiInstanceLoopCharacteristics,
)

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class MultiInstanceLoopCharacteristics(TMultiInstanceLoopCharacteristics):
    class Meta:
        name = "multiInstanceLoopCharacteristics"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
