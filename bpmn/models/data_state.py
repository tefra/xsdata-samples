from __future__ import annotations

from dataclasses import dataclass

from .t_data_state import TDataState

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class DataState(TDataState):
    class Meta:
        name = "dataState"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
