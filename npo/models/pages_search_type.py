from __future__ import annotations

from dataclasses import dataclass, field

from npo.models.date_range_matcher_list_type import DateRangeMatcherListType
from npo.models.extended_text_matcher_list_type import (
    ExtendedTextMatcherListType,
)
from npo.models.match import Match
from npo.models.page_association_search_list_type import (
    PageAssociationSearchListType,
)
from npo.models.page_relation_search_list_type import (
    PageRelationSearchListType,
)
from npo.models.simple_matcher_type import SimpleMatcherType
from npo.models.text_matcher_list_type import TextMatcherListType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class PagesSearchType:
    class Meta:
        name = "pagesSearchType"

    text: None | SimpleMatcherType = field(
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
    types: None | TextMatcherListType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    portals: None | TextMatcherListType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    sections: None | TextMatcherListType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    genres: None | TextMatcherListType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    tags: None | ExtendedTextMatcherListType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    keywords: None | ExtendedTextMatcherListType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    sort_dates: None | DateRangeMatcherListType = field(
        default=None,
        metadata={
            "name": "sortDates",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    last_modified_dates: None | DateRangeMatcherListType = field(
        default=None,
        metadata={
            "name": "lastModifiedDates",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    creation_dates: None | DateRangeMatcherListType = field(
        default=None,
        metadata={
            "name": "creationDates",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    publish_dates: None | DateRangeMatcherListType = field(
        default=None,
        metadata={
            "name": "publishDates",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    relations: None | PageRelationSearchListType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    links: None | PageAssociationSearchListType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    referrals: None | PageAssociationSearchListType = field(
        default=None,
        metadata={
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
