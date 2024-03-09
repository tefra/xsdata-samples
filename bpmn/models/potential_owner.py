from dataclasses import dataclass

from .t_potential_owner import TPotentialOwner

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class PotentialOwner(TPotentialOwner):
    class Meta:
        name = "potentialOwner"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
