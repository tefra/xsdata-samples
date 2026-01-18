from __future__ import annotations

from dataclasses import dataclass, field

from npo.models.media_facets_result_type import MediaFacetsResultType
from npo.models.page_facets_result_type import PageFacetsResultType
from npo.models.search_result_type import SearchResultType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass(kw_only=True)
class PageSearchResultType(SearchResultType):
    class Meta:
        name = "pageSearchResultType"

    facets: None | PageFacetsResultType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    selected_facets: None | PageFacetsResultType = field(
        default=None,
        metadata={
            "name": "selectedFacets",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    media_facets: None | MediaFacetsResultType = field(
        default=None,
        metadata={
            "name": "mediaFacets",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    media_selected_facets: None | MediaFacetsResultType = field(
        default=None,
        metadata={
            "name": "mediaSelectedFacets",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
