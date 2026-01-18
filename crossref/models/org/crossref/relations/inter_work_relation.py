from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.org.crossref.relations.inter_work_relation_identifier_type import (
    InterWorkRelationIdentifierType,
)
from crossref.models.org.crossref.relations.inter_work_relation_relationship_type import (
    InterWorkRelationRelationshipType,
)

__NAMESPACE__ = "http://www.crossref.org/relations.xsd"


@dataclass
class InterWorkRelation:
    """
    :ivar relationship_type: Used to describe relations between items
        that are not the same work.
    :ivar identifier_type:
    :ivar namespace: An identifier systems may require a namespace that
        is needed in addition to the identifer value to provide
        uniqueness.
    :ivar content:
    """

    class Meta:
        name = "inter_work_relation"
        namespace = "http://www.crossref.org/relations.xsd"

    relationship_type: InterWorkRelationRelationshipType | None = field(
        default=None,
        metadata={
            "name": "relationship-type",
            "type": "Attribute",
            "required": True,
        },
    )
    identifier_type: InterWorkRelationIdentifierType | None = field(
        default=None,
        metadata={
            "name": "identifier-type",
            "type": "Attribute",
            "required": True,
        },
    )
    namespace: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_length": 4,
            "max_length": 1024,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )
