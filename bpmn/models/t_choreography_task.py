from dataclasses import dataclass, field
from typing import List
from xml.etree.ElementTree import QName
from .t_choreography_activity import TChoreographyActivity

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TChoreographyTask(TChoreographyActivity):
    class Meta:
        name = "tChoreographyTask"

    message_flow_ref: List[QName] = field(
        default_factory=list,
        metadata={
            "name": "messageFlowRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )
