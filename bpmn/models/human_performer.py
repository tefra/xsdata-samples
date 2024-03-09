from dataclasses import dataclass

from .t_human_performer import THumanPerformer

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class HumanPerformer(THumanPerformer):
    class Meta:
        name = "humanPerformer"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
