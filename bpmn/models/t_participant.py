from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName

from .participant_multiplicity import ParticipantMultiplicity
from .t_base_element import TBaseElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
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
    participant_multiplicity: Optional[ParticipantMultiplicity] = field(
        default=None,
        metadata={
            "name": "participantMultiplicity",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    process_ref: Optional[QName] = field(
        default=None,
        metadata={
            "name": "processRef",
            "type": "Attribute",
        },
    )
