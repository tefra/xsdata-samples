from __future__ import annotations

from dataclasses import dataclass

from .t_root_element import TRootElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TEndPoint(TRootElement):
    class Meta:
        name = "tEndPoint"
