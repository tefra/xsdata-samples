from dataclasses import dataclass
from .t_artifact import TArtifact

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class Artifact(TArtifact):
    class Meta:
        name = "artifact"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
