from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

from .correlation_key import CorrelationKey
from .t_choreography_loop_type import TChoreographyLoopType
from .t_flow_node import TFlowNode

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class TChoreographyActivity(TFlowNode):
    class Meta:
        name = "tChoreographyActivity"

    participant_ref: list[QName] = field(
        default_factory=list,
        metadata={
            "name": "participantRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
            "min_occurs": 2,
        },
    )
    correlation_key: list[CorrelationKey] = field(
        default_factory=list,
        metadata={
            "name": "correlationKey",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    initiating_participant_ref: QName = field(
        metadata={
            "name": "initiatingParticipantRef",
            "type": "Attribute",
            "required": True,
        }
    )
    loop_type: TChoreographyLoopType = field(
        default=TChoreographyLoopType.NONE,
        metadata={
            "name": "loopType",
            "type": "Attribute",
        },
    )
