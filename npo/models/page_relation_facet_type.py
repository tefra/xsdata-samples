from __future__ import annotations

from dataclasses import dataclass, field

from npo.models.extended_page_facet_type import ExtendedPageFacetType
from npo.models.page_relation_search_type import PageRelationSearchType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass(kw_only=True)
class PageRelationFacetType(ExtendedPageFacetType):
    class Meta:
        name = "pageRelationFacetType"

    sub_search: None | PageRelationSearchType = field(
        default=None,
        metadata={
            "name": "subSearch",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
