from dataclasses import dataclass, field
from typing import List
from npo.models.page_relation_search_type import PageRelationSearchType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class PageRelationSearchListType:
    class Meta:
        name = "pageRelationSearchListType"

    relation_search: List[PageRelationSearchType] = field(
        default_factory=list,
        metadata={
            "name": "relationSearch",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
