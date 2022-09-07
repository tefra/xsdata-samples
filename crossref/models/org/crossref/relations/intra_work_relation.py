from dataclasses import dataclass, field
from typing import List, Optional
from crossref.models.org.crossref.relations.intra_work_relation_relationship_type import IntraWorkRelationRelationshipType
from crossref.models.org.crossref.relations.relations_type_atts_identifier_type import RelationsTypeAttsIdentifierType

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

    relationship_type: Optional[IntraWorkRelationRelationshipType] = field(
        default=None,
        metadata={
            "name": "relationship-type",
            "type": "Attribute",
            "required": True,
        }
    )
    identifier_type: Optional[RelationsTypeAttsIdentifierType] = field(
        default=None,
        metadata={
            "name": "identifier-type",
            "type": "Attribute",
            "required": True,
        }
    )
    namespace: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_length": 4,
            "max_length": 1024,
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
