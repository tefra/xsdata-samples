from __future__ import annotations

from dataclasses import dataclass, field

from npo.models.media_facet_type import MediaFacetType
from npo.models.member_ref_search_type import MemberRefSearchType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass(kw_only=True)
class MemberRefFacetType(MediaFacetType):
    class Meta:
        name = "memberRefFacetType"

    sub_search: None | MemberRefSearchType = field(
        default=None,
        metadata={
            "name": "subSearch",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
