from dataclasses import dataclass, field
from typing import Optional
from npo.models.match import Match
from npo.models.text_matcher_list_type import TextMatcherListType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class MemberRefSearchType:
    class Meta:
        name = "memberRefSearchType"

    media_ids: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "name": "mediaIds",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    types: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    match: Optional[Match] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )