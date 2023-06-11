from __future__ import annotations
from dataclasses import dataclass, field
from npo.models.text_facet_type import TextFacetType
from npo.models.title_search_type import TitleSearchType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class MediaTitleFacetType(TextFacetType):
    class Meta:
        name = "mediaTitleFacetType"

    sub_search: None | TitleSearchType = field(
        default=None,
        metadata={
            "name": "subSearch",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
