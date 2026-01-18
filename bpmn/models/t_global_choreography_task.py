from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

from .t_choreography import TChoreography

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TGlobalChoreographyTask(TChoreography):
    class Meta:
        name = "tGlobalChoreographyTask"

    initiating_participant_ref: QName | None = field(
        default=None,
        metadata={
            "name": "initiatingParticipantRef",
            "type": "Attribute",
        },
    )
