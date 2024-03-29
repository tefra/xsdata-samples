from __future__ import annotations

from dataclasses import dataclass, field

from npo.models.extended_text_matcher_list_type import (
    ExtendedTextMatcherListType,
)
from npo.models.match import Match
from npo.models.text_matcher_list_type import TextMatcherListType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class PageRelationSearchType:
    class Meta:
        name = "pageRelationSearchType"

    types: None | TextMatcherListType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    broadcasters: None | TextMatcherListType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    values: None | ExtendedTextMatcherListType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    uri_refs: None | TextMatcherListType = field(
        default=None,
        metadata={
            "name": "uriRefs",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    match: None | Match = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
