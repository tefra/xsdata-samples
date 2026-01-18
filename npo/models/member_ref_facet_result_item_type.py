from __future__ import annotations

from dataclasses import dataclass, field

from npo.models.media_type_enum import MediaTypeEnum
from npo.models.term_facet_result_item_type import TermFacetResultItemType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass(kw_only=True)
class MemberRefFacetResultItemType(TermFacetResultItemType):
    class Meta:
        name = "memberRefFacetResultItemType"

    type_value: None | MediaTypeEnum = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
