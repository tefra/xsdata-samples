from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName

from .t_base_element import TBaseElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TParticipantAssociation(TBaseElement):
    class Meta:
        name = "tParticipantAssociation"

    inner_participant_ref: Optional[QName] = field(
        default=None,
        metadata={
            "name": "innerParticipantRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
            "required": True,
        },
    )
    outer_participant_ref: Optional[QName] = field(
        default=None,
        metadata={
            "name": "outerParticipantRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
            "required": True,
        },
    )
