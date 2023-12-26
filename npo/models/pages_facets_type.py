from __future__ import annotations
from dataclasses import dataclass, field
from npo.models.date_range_facets_type import DateRangeFacetsType
from npo.models.extended_page_facet_type import ExtendedPageFacetType
from npo.models.page_facet_type import PageFacetType
from npo.models.page_relation_facet_list_type import PageRelationFacetListType
from npo.models.page_searchable_term_facet_type import (
    PageSearchableTermFacetType,
)
from npo.models.pages_search_type import PagesSearchType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class PagesFacetsType:
    class Meta:
        name = "pagesFacetsType"

    sort_dates: None | DateRangeFacetsType = field(
        default=None,
        metadata={
            "name": "sortDates",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    broadcasters: None | PageFacetType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    types: None | PageFacetType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    tags: None | ExtendedPageFacetType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    keywords: None | ExtendedPageFacetType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    genres: None | PageSearchableTermFacetType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    portals: None | PageFacetType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    sections: None | PageFacetType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    relations: None | PageRelationFacetListType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    filter: None | PagesSearchType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
