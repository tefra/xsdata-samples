from __future__ import annotations

from dataclasses import dataclass

from .t_standard_loop_characteristics import TStandardLoopCharacteristics

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class StandardLoopCharacteristics(TStandardLoopCharacteristics):
    class Meta:
        name = "standardLoopCharacteristics"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
