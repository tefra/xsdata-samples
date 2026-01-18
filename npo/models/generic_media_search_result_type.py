from __future__ import annotations

from dataclasses import dataclass, field

from npo.models.media_facets_result_type import MediaFacetsResultType
from npo.models.search_result_type import SearchResultType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass(kw_only=True)
class GenericMediaSearchResultType(SearchResultType):
    class Meta:
        name = "genericMediaSearchResultType"

    facets: None | MediaFacetsResultType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    selected_facets: None | MediaFacetsResultType = field(
        default=None,
        metadata={
            "name": "selectedFacets",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
