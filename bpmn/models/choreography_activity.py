from dataclasses import dataclass
from .t_choreography_activity import TChoreographyActivity

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class ChoreographyActivity(TChoreographyActivity):
    class Meta:
        name = "choreographyActivity"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
