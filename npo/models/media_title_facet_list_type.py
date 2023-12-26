from __future__ import annotations
from dataclasses import dataclass, field
from npo.models.media_facet_type import MediaFacetType
from npo.models.media_title_facet_type import MediaTitleFacetType
from npo.models.title_search_type import TitleSearchType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class MediaTitleFacetListType(MediaFacetType):
    class Meta:
        name = "mediaTitleFacetListType"

    sub_search: None | TitleSearchType = field(
        default=None,
        metadata={
            "name": "subSearch",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    title: list[MediaTitleFacetType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
