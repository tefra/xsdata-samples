from __future__ import annotations
from dataclasses import dataclass, field
from npo.models.media_facets_type import MediaFacetsType
from npo.models.media_search_type import MediaSearchType
from npo.models.media_sort_type import MediaSortType
from npo.models.title_sort_order_type import TitleSortOrderType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class MediaFormType:
    class Meta:
        name = "mediaFormType"

    searches: None | MediaSearchType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    sort_fields: None | MediaFormType.SortFields = field(
        default=None,
        metadata={
            "name": "sortFields",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    facets: None | MediaFacetsType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    highlight: None | bool = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

    @dataclass
    class SortFields:
        sort: list[MediaSortType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:vpro:api:2013",
            }
        )
        title_sort: list[TitleSortOrderType] = field(
            default_factory=list,
            metadata={
                "name": "titleSort",
                "type": "Element",
                "namespace": "urn:vpro:api:2013",
            }
        )
