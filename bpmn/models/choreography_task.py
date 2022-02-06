from dataclasses import dataclass
from .t_choreography_task import TChoreographyTask

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class ChoreographyTask(TChoreographyTask):
    class Meta:
        name = "choreographyTask"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
