from dataclasses import dataclass, field
from typing import Optional

from crossref.models.org.crossref.relations.description import Description
from crossref.models.org.crossref.relations.inter_work_relation import (
    InterWorkRelation,
)
from crossref.models.org.crossref.relations.intra_work_relation import (
    IntraWorkRelation,
)

__NAMESPACE__ = "http://www.crossref.org/relations.xsd"


@dataclass
class RelatedItem:
    class Meta:
        name = "related_item"
        namespace = "http://www.crossref.org/relations.xsd"

    description: Description | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    inter_work_relation: InterWorkRelation | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    intra_work_relation: IntraWorkRelation | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
