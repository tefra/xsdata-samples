from dataclasses import dataclass, field
from typing import Optional
from npo.models.media_type_enum import MediaTypeEnum
from npo.models.term_facet_result_item_type import TermFacetResultItemType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class MemberRefFacetResultItemType(TermFacetResultItemType):
    class Meta:
        name = "memberRefFacetResultItemType"

    type: Optional[MediaTypeEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
