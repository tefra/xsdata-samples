from dataclasses import dataclass
from .t_resource_role import TResourceRole

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TPerformer(TResourceRole):
    class Meta:
        name = "tPerformer"
