from __future__ import annotations
from dataclasses import dataclass, field
from npo.models.media_search_type import MediaSearchType
from npo.models.text_facet_type import TextFacetType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class ExtendedMediaFacetType(TextFacetType):
    class Meta:
        name = "extendedMediaFacetType"

    filter: None | MediaSearchType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    case_sensitive: None | bool = field(
        default=None,
        metadata={
            "name": "caseSensitive",
            "type": "Attribute",
        },
    )
