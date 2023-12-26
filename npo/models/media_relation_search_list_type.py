from __future__ import annotations
from dataclasses import dataclass, field
from npo.models.media_relation_search_type import MediaRelationSearchType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class MediaRelationSearchListType:
    class Meta:
        name = "mediaRelationSearchListType"

    relation_search: list[MediaRelationSearchType] = field(
        default_factory=list,
        metadata={
            "name": "relationSearch",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
