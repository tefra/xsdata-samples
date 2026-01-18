from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

from .t_artifact import TArtifact
from .t_association_direction import TAssociationDirection

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class TAssociation(TArtifact):
    class Meta:
        name = "tAssociation"

    source_ref: QName = field(
        metadata={
            "name": "sourceRef",
            "type": "Attribute",
            "required": True,
        }
    )
    target_ref: QName = field(
        metadata={
            "name": "targetRef",
            "type": "Attribute",
            "required": True,
        }
    )
    association_direction: TAssociationDirection = field(
        default=TAssociationDirection.NONE,
        metadata={
            "name": "associationDirection",
            "type": "Attribute",
        },
    )
