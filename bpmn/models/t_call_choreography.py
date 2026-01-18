from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

from .participant_association import ParticipantAssociation
from .t_choreography_activity import TChoreographyActivity

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TCallChoreography(TChoreographyActivity):
    class Meta:
        name = "tCallChoreography"

    participant_association: list[ParticipantAssociation] = field(
        default_factory=list,
        metadata={
            "name": "participantAssociation",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    called_choreography_ref: None | QName = field(
        default=None,
        metadata={
            "name": "calledChoreographyRef",
            "type": "Attribute",
        },
    )
