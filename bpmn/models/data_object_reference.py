from dataclasses import dataclass
from .t_data_object_reference import TDataObjectReference

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class DataObjectReference(TDataObjectReference):
    class Meta:
        name = "dataObjectReference"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
