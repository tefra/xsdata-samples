from __future__ import annotations

from dataclasses import dataclass, field

from npo.models.date_facet_result_item_type import DateFacetResultItemType
from npo.models.named_term_facet_result_item_type import (
    NamedTermFacetResultItemType,
)
from npo.models.page_genre_facet_result_item_type import (
    PageGenreFacetResultItemType,
)
from npo.models.term_facet_result_item_type import TermFacetResultItemType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass(kw_only=True)
class PageFacetsResultType:
    class Meta:
        name = "pageFacetsResultType"

    sort_dates: list[None | DateFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "name": "sortDates",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        },
    )
    types: list[None | TermFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        },
    )
    broadcasters: list[None | TermFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        },
    )
    tags: list[None | TermFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        },
    )
    keywords: list[None | TermFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        },
    )
    genres: list[None | PageGenreFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        },
    )
    portals: list[None | TermFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        },
    )
    sections: list[None | TermFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        },
    )
    relations: list[None | NamedTermFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        },
    )
