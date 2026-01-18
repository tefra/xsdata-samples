from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

from .t_base_element import TBaseElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class TParticipantAssociation(TBaseElement):
    class Meta:
        name = "tParticipantAssociation"

    inner_participant_ref: QName = field(
        metadata={
            "name": "innerParticipantRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
            "required": True,
        }
    )
    outer_participant_ref: QName = field(
        metadata={
            "name": "outerParticipantRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
            "required": True,
        }
    )
