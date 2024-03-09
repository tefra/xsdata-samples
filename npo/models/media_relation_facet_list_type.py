from __future__ import annotations

from dataclasses import dataclass, field

from npo.models.abstract_facet_type import AbstractFacetType
from npo.models.media_relation_facet_type import MediaRelationFacetType
from npo.models.media_relation_search_type import MediaRelationSearchType
from npo.models.media_search_type import MediaSearchType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class MediaRelationFacetListType(AbstractFacetType):
    class Meta:
        name = "mediaRelationFacetListType"

    filter: None | MediaSearchType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    sub_search: None | MediaRelationSearchType = field(
        default=None,
        metadata={
            "name": "subSearch",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    facet: list[MediaRelationFacetType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
