from __future__ import annotations

from dataclasses import dataclass, field

from npo.models.media_form import MediaForm
from npo.models.page_sort_list_type import PageSortListType
from npo.models.pages_facets_type import PagesFacetsType
from npo.models.pages_search_type import PagesSearchType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass(kw_only=True)
class PagesFormType:
    class Meta:
        name = "pagesFormType"

    searches: None | PagesSearchType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    sort_fields: None | PageSortListType = field(
        default=None,
        metadata={
            "name": "sortFields",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    facets: None | PagesFacetsType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    media_form: None | MediaForm = field(
        default=None,
        metadata={
            "name": "mediaForm",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    highlight: None | bool = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
