from dataclasses import dataclass, field
from typing import List
from npo.models.media_relation_search_type import MediaRelationSearchType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class MediaRelationSearchListType:
    class Meta:
        name = "mediaRelationSearchListType"

    relation_search: List[MediaRelationSearchType] = field(
        default_factory=list,
        metadata={
            "name": "relationSearch",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
