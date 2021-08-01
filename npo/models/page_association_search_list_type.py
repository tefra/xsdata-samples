from dataclasses import dataclass, field
from typing import List
from npo.models.association_search_type import AssociationSearchType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class PageAssociationSearchListType:
    class Meta:
        name = "pageAssociationSearchListType"

    search: List[AssociationSearchType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
