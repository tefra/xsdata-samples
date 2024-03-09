from __future__ import annotations

from dataclasses import dataclass, field

from npo.models.page_facet_type import PageFacetType
from npo.models.term_search_type import TermSearchType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class PageSearchableTermFacetType(PageFacetType):
    class Meta:
        name = "pageSearchableTermFacetType"

    sub_search: None | TermSearchType = field(
        default=None,
        metadata={
            "name": "subSearch",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
