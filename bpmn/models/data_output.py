from __future__ import annotations

from dataclasses import dataclass

from .t_data_output import TDataOutput

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class DataOutput(TDataOutput):
    class Meta:
        name = "dataOutput"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
