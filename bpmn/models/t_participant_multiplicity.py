from dataclasses import dataclass, field

from .t_base_element import TBaseElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TParticipantMultiplicity(TBaseElement):
    class Meta:
        name = "tParticipantMultiplicity"

    minimum: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        },
    )
    maximum: int = field(
        default=1,
        metadata={
            "type": "Attribute",
        },
    )
