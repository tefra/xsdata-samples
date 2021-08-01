from dataclasses import dataclass, field
from typing import Optional
from npo.models.extended_page_facet_type import ExtendedPageFacetType
from npo.models.page_relation_search_type import PageRelationSearchType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class PageRelationFacetType(ExtendedPageFacetType):
    class Meta:
        name = "pageRelationFacetType"

    sub_search: Optional[PageRelationSearchType] = field(
        default=None,
        metadata={
            "name": "subSearch",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
