from __future__ import annotations

from dataclasses import dataclass, field

from npo.models.date_facet_result_item_type import DateFacetResultItemType
from npo.models.duration_facet_result_item_type import (
    DurationFacetResultItemType,
)
from npo.models.media_genre_facet_result_item_type import (
    MediaGenreFacetResultItemType,
)
from npo.models.media_geo_location_facet_result_item_type import (
    MediaGeoLocationFacetResultItemType,
)
from npo.models.member_ref_facet_result_item_type import (
    MemberRefFacetResultItemType,
)
from npo.models.named_term_facet_result_item_type import (
    NamedTermFacetResultItemType,
)
from npo.models.term_facet_result_item_type import TermFacetResultItemType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class MediaFacetsResultType:
    class Meta:
        name = "mediaFacetsResultType"

    titles: list[TermFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        },
    )
    types: list[TermFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        },
    )
    av_types: list[TermFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "name": "avTypes",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        },
    )
    sort_dates: list[DateFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "name": "sortDates",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        },
    )
    broadcasters: list[TermFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        },
    )
    genres: list[MediaGenreFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        },
    )
    geo_locations: list[MediaGeoLocationFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "name": "geoLocations",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        },
    )
    tags: list[TermFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        },
    )
    durations: list[DurationFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        },
    )
    descendant_of: list[MemberRefFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "name": "descendantOf",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        },
    )
    episode_of: list[MemberRefFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "name": "episodeOf",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        },
    )
    member_of: list[MemberRefFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "name": "memberOf",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        },
    )
    relations: list[NamedTermFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        },
    )
    age_ratings: list[TermFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "name": "ageRatings",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        },
    )
    content_ratings: list[TermFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "name": "contentRatings",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        },
    )
