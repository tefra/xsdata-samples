from __future__ import annotations
from dataclasses import dataclass, field
from npo.models.date_range_facets_type import DateRangeFacetsType
from npo.models.duration_range_facets_type import DurationRangeFacetsType
from npo.models.extended_media_facet_type import ExtendedMediaFacetType
from npo.models.media_facet_type import MediaFacetType
from npo.models.media_relation_facet_list_type import (
    MediaRelationFacetListType,
)
from npo.models.media_search_type import MediaSearchType
from npo.models.media_searchable_term_facet_type import (
    MediaSearchableTermFacetType,
)
from npo.models.media_title_facet_list_type import MediaTitleFacetListType
from npo.models.member_ref_facet_type import MemberRefFacetType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class MediaFacetsType:
    class Meta:
        name = "mediaFacetsType"

    titles: None | MediaTitleFacetListType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    types: None | MediaFacetType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    av_types: None | MediaFacetType = field(
        default=None,
        metadata={
            "name": "avTypes",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    sort_dates: None | DateRangeFacetsType = field(
        default=None,
        metadata={
            "name": "sortDates",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    broadcasters: None | MediaFacetType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    genres: None | MediaSearchableTermFacetType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    tags: None | ExtendedMediaFacetType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    durations: None | DurationRangeFacetsType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    descendant_of: None | MemberRefFacetType = field(
        default=None,
        metadata={
            "name": "descendantOf",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    episode_of: None | MemberRefFacetType = field(
        default=None,
        metadata={
            "name": "episodeOf",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    member_of: None | MemberRefFacetType = field(
        default=None,
        metadata={
            "name": "memberOf",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    relations: None | MediaRelationFacetListType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    age_ratings: None | MediaFacetType = field(
        default=None,
        metadata={
            "name": "ageRatings",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    content_ratings: None | MediaFacetType = field(
        default=None,
        metadata={
            "name": "contentRatings",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    geo_locations: None | MediaSearchableTermFacetType = field(
        default=None,
        metadata={
            "name": "geoLocations",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    filter: None | MediaSearchType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
