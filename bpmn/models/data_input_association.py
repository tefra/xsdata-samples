from dataclasses import dataclass
from .t_data_input_association import TDataInputAssociation

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class DataInputAssociation(TDataInputAssociation):
    class Meta:
        name = "dataInputAssociation"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
