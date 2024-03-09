from dataclasses import dataclass

from .t_data_input import TDataInput

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class DataInput(TDataInput):
    class Meta:
        name = "dataInput"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
