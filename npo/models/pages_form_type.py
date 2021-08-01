from dataclasses import dataclass, field
from typing import Optional
from npo.models.media_form import MediaForm
from npo.models.page_sort_list_type import PageSortListType
from npo.models.pages_facets_type import PagesFacetsType
from npo.models.pages_search_type import PagesSearchType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class PagesFormType:
    class Meta:
        name = "pagesFormType"

    searches: Optional[PagesSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    sort_fields: Optional[PageSortListType] = field(
        default=None,
        metadata={
            "name": "sortFields",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    facets: Optional[PagesFacetsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    media_form: Optional[MediaForm] = field(
        default=None,
        metadata={
            "name": "mediaForm",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    highlight: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
