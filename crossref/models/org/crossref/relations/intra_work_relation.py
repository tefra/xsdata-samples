from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.org.crossref.relations.intra_work_relation_identifier_type import (
    IntraWorkRelationIdentifierType,
)
from crossref.models.org.crossref.relations.intra_work_relation_relationship_type import (
    IntraWorkRelationRelationshipType,
)

__NAMESPACE__ = "http://www.crossref.org/relations.xsd"


@dataclass
class IntraWorkRelation:
    """
    :ivar relationship_type: Used to define relations between items that
        are essentially the same work but may differ in some way that
        impacts citation, for example a difference in format, language,
        or revision. Assigning different identifers to exactly the same
        item available in one place or as copies in multiple places can
        be problematic and should be avoided.
    :ivar identifier_type:
    :ivar namespace: An identifier systems may require a namespace that
        is needed in addition to the identifer value to provide
        uniqueness.
    :ivar content:
    """

    class Meta:
        name = "intra_work_relation"
        namespace = "http://www.crossref.org/relations.xsd"

    relationship_type: IntraWorkRelationRelationshipType | None = field(
        default=None,
        metadata={
            "name": "relationship-type",
            "type": "Attribute",
            "required": True,
        },
    )
    identifier_type: IntraWorkRelationIdentifierType | None = field(
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
