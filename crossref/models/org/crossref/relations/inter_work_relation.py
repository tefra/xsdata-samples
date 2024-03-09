from dataclasses import dataclass, field
from typing import List, Optional

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

    relationship_type: Optional[InterWorkRelationRelationshipType] = field(
        default=None,
        metadata={
            "name": "relationship-type",
            "type": "Attribute",
            "required": True,
        },
    )
    identifier_type: Optional[InterWorkRelationIdentifierType] = field(
        default=None,
        metadata={
            "name": "identifier-type",
            "type": "Attribute",
            "required": True,
        },
    )
    namespace: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_length": 4,
            "max_length": 1024,
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )
