from __future__ import annotations

from dataclasses import dataclass

from .t_data_input import TDataInput

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class DataInput(TDataInput):
    class Meta:
        name = "dataInput"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
