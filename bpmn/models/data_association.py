from dataclasses import dataclass
from .t_data_association import TDataAssociation

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class DataAssociation(TDataAssociation):
    class Meta:
        name = "dataAssociation"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
