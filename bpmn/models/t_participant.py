from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

from .participant_multiplicity import ParticipantMultiplicity
from .t_base_element import TBaseElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class TParticipant(TBaseElement):
    class Meta:
        name = "tParticipant"

    interface_ref: list[QName] = field(
        default_factory=list,
        metadata={
            "name": "interfaceRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    end_point_ref: list[QName] = field(
        default_factory=list,
        metadata={
            "name": "endPointRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    participant_multiplicity: None | ParticipantMultiplicity = field(
        default=None,
        metadata={
            "name": "participantMultiplicity",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    process_ref: None | QName = field(
        default=None,
        metadata={
            "name": "processRef",
            "type": "Attribute",
        },
    )
