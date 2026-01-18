from dataclasses import dataclass, field

from generali.models.org.w3.pkg_2005.pkg_08.addressing.relationship_type import (
    RelationshipType,
)

__NAMESPACE__ = "http://www.w3.org/2005/08/addressing"


@dataclass
class RelatesToType:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    relationship_type: RelationshipType | str = field(
        default=RelationshipType.HTTP_WWW_W3_ORG_2005_08_ADDRESSING_REPLY,
        metadata={
            "name": "RelationshipType",
            "type": "Attribute",
        },
    )
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
