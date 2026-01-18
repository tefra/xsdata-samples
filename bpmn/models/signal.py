from __future__ import annotations

from dataclasses import dataclass

from .t_signal import TSignal

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class Signal(TSignal):
    class Meta:
        name = "signal"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
