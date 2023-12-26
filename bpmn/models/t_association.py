from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName
from .t_artifact import TArtifact
from .t_association_direction import TAssociationDirection

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TAssociation(TArtifact):
    class Meta:
        name = "tAssociation"

    source_ref: Optional[QName] = field(
        default=None,
        metadata={
            "name": "sourceRef",
            "type": "Attribute",
            "required": True,
        },
    )
    target_ref: Optional[QName] = field(
        default=None,
        metadata={
            "name": "targetRef",
            "type": "Attribute",
            "required": True,
        },
    )
    association_direction: TAssociationDirection = field(
        default=TAssociationDirection.NONE,
        metadata={
            "name": "associationDirection",
            "type": "Attribute",
        },
    )
