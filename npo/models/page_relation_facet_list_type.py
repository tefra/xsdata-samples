from __future__ import annotations
from dataclasses import dataclass, field
from npo.models.abstract_facet_type import AbstractFacetType
from npo.models.page_relation_facet_type import PageRelationFacetType
from npo.models.page_relation_search_type import PageRelationSearchType
from npo.models.pages_search_type import PagesSearchType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class PageRelationFacetListType(AbstractFacetType):
    class Meta:
        name = "pageRelationFacetListType"

    filter: None | PagesSearchType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    sub_search: None | PageRelationSearchType = field(
        default=None,
        metadata={
            "name": "subSearch",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    facet: list[PageRelationFacetType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
