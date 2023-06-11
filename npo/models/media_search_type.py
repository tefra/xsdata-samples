from __future__ import annotations
from dataclasses import dataclass, field
from npo.models.date_range_matcher_list_type import DateRangeMatcherListType
from npo.models.duration_range_matcher_list_type import DurationRangeMatcherListType
from npo.models.extended_text_matcher_list_type import ExtendedTextMatcherListType
from npo.models.geo_location_search_type import GeoLocationSearchType
from npo.models.match import Match
from npo.models.media_relation_search_list_type import MediaRelationSearchListType
from npo.models.schedule_event_search_type import ScheduleEventSearchType
from npo.models.simple_matcher_type import SimpleMatcherType
from npo.models.text_matcher_list_type import TextMatcherListType
from npo.models.title_search_type import TitleSearchType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class MediaSearchType:
    """
    Limits the search result to media with certain properties.
    """
    class Meta:
        name = "mediaSearchType"

    text: None | SimpleMatcherType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    media_ids: None | TextMatcherListType = field(
        default=None,
        metadata={
            "name": "mediaIds",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "doc": "The MID must match one of the mediaIds",
        }
    )
    types: None | TextMatcherListType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "doc": "The media type must match one of these.",
        }
    )
    av_types: None | TextMatcherListType = field(
        default=None,
        metadata={
            "name": "avTypes",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    sort_dates: None | DateRangeMatcherListType = field(
        default=None,
        metadata={
            "name": "sortDates",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    publish_dates: None | DateRangeMatcherListType = field(
        default=None,
        metadata={
            "name": "publishDates",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    creation_dates: None | DateRangeMatcherListType = field(
        default=None,
        metadata={
            "name": "creationDates",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    last_modified_dates: None | DateRangeMatcherListType = field(
        default=None,
        metadata={
            "name": "lastModifiedDates",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    broadcasters: None | TextMatcherListType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    locations: None | TextMatcherListType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    tags: None | ExtendedTextMatcherListType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    genres: None | TextMatcherListType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    durations: None | DurationRangeMatcherListType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    descendant_of: None | TextMatcherListType = field(
        default=None,
        metadata={
            "name": "descendantOf",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    episode_of: None | TextMatcherListType = field(
        default=None,
        metadata={
            "name": "episodeOf",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    member_of: None | TextMatcherListType = field(
        default=None,
        metadata={
            "name": "memberOf",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    relations: None | MediaRelationSearchListType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    schedule_events: list[ScheduleEventSearchType] = field(
        default_factory=list,
        metadata={
            "name": "scheduleEvents",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    age_ratings: None | TextMatcherListType = field(
        default=None,
        metadata={
            "name": "ageRatings",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    content_ratings: None | TextMatcherListType = field(
        default=None,
        metadata={
            "name": "contentRatings",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    titles: list[TitleSearchType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    geo_locations: list[GeoLocationSearchType] = field(
        default_factory=list,
        metadata={
            "name": "geoLocations",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    match: None | Match = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
