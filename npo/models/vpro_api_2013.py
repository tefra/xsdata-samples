from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlDuration
from npo.models.vpro_media_2009 import (
    ChannelEnum,
    GeoRoleType,
    Group,
    MediaTypeEnum,
    Program,
    ScheduleEventType,
    Segment,
    TextualTypeEnum,
)
from npo.models.vpro_shared_2009 import OwnerTypeEnum

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class AbstractFacetType:
    class Meta:
        name = "abstractFacetType"


@dataclass
class DateRangeFacetItemType:
    class Meta:
        name = "dateRangeFacetItemType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    begin: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    end: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


class DateRangePresetTypeEnum(Enum):
    BEFORE_LAST_YEAR = "BEFORE_LAST_YEAR"
    LAST_YEAR = "LAST_YEAR"
    LAST_MONTH = "LAST_MONTH"
    LAST_WEEK = "LAST_WEEK"
    YESTERDAY = "YESTERDAY"
    TODAY = "TODAY"
    THIS_WEEK = "THIS_WEEK"
    TOMORROW = "TOMORROW"


@dataclass
class DurationRangeFacetItemType:
    class Meta:
        name = "durationRangeFacetItemType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    begin: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    end: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


class FacetOrderTypeEnum(Enum):
    VALUE_ASC = "VALUE_ASC"
    VALUE_DESC = "VALUE_DESC"
    COUNT_ASC = "COUNT_ASC"
    COUNT_DESC = "COUNT_DESC"
    TERM = "TERM"
    REVERSE_TERM = "REVERSE_TERM"
    COUNT = "COUNT"
    REVERSE_COUNT = "REVERSE_COUNT"


@dataclass
class FacetResultItem:
    class Meta:
        name = "facetResultItem"

    count: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "required": True,
        }
    )
    selected: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class HightlightType:
    class Meta:
        name = "hightlightType"

    body: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    term: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


class Match(Enum):
    MUST = "MUST"
    SHOULD = "SHOULD"
    NOT_VALUE = "NOT"


@dataclass
class MediaSearchResults:
    class Meta:
        name = "mediaSearchResults"


class MediaSortTypeEnum(Enum):
    TITLE = "title"
    SORT_DATE = "sortDate"
    PUBLISH_DATE = "publishDate"
    EPISODE = "episode"
    EPISODE_ADDED = "episodeAdded"
    MEMBER_ADDED = "memberAdded"
    MEMBER = "member"
    CREATION_DATE = "creationDate"
    LAST_MODIFIED = "lastModified"


class OrderTypeEnum(Enum):
    ASC = "ASC"
    DESC = "DESC"


@dataclass
class PageSearchResults:
    class Meta:
        name = "pageSearchResults"


class PageSortTypeEnum(Enum):
    SORT_DATE = "sortDate"
    LAST_MODIFIED = "lastModified"
    LAST_PUBLISHED = "lastPublished"
    CREATION_DATE = "creationDate"


@dataclass
class RedirectEntry:
    class Meta:
        name = "redirectEntry"
        namespace = "urn:vpro:api:2013"

    from_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "from",
            "type": "Attribute",
            "required": True,
        }
    )
    to: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    ultimate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    circular: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class SimpleMatchType(Enum):
    TEXT = "TEXT"


class StandardMatchType(Enum):
    TEXT = "TEXT"
    REGEX = "REGEX"
    WILDCARD = "WILDCARD"


@dataclass
class Suggestion:
    class Meta:
        name = "suggestion"
        namespace = "urn:vpro:api:2013"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


class TotalQualifier(Enum):
    EQUAL_TO = "EQUAL_TO"
    APPROXIMATE = "APPROXIMATE"
    GREATER_THAN_OR_EQUAL_TO = "GREATER_THAN_OR_EQUAL_TO"
    MISSING = "MISSING"


@dataclass
class DateRangeFacetsType(AbstractFacetType):
    class Meta:
        name = "dateRangeFacetsType"

    interval: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "sequential": True,
        }
    )
    preset: List[DateRangePresetTypeEnum] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "sequential": True,
        }
    )
    range: List[DateRangeFacetItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "sequential": True,
        }
    )


@dataclass
class DurationRangeFacetsType(AbstractFacetType):
    class Meta:
        name = "durationRangeFacetsType"

    interval: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "sequential": True,
        }
    )
    range: List[DurationRangeFacetItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "sequential": True,
        }
    )


@dataclass
class ExtendedMatcherType:
    class Meta:
        name = "extendedMatcherType"

    value: Optional[str] = field(
        default=None,
    )
    fuzziness: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    match_type: Optional[StandardMatchType] = field(
        default=None,
        metadata={
            "name": "matchType",
            "type": "Attribute",
        }
    )
    case_sensitive: Optional[bool] = field(
        default=None,
        metadata={
            "name": "caseSensitive",
            "type": "Attribute",
        }
    )
    match: Optional[Match] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class GeoLocationSearchType:
    class Meta:
        name = "geoLocationSearchType"

    value: Optional[str] = field(
        default=None,
    )
    owner: Optional[OwnerTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    role: Optional[GeoRoleType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    gtaa_uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "gtaaUri",
            "type": "Attribute",
        }
    )
    match: Optional[Match] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class MatcherList:
    class Meta:
        name = "matcherList"

    match: Optional[Match] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class MediaSortType:
    class Meta:
        name = "mediaSortType"

    value: Optional[MediaSortTypeEnum] = field(
        default=None,
    )
    order: Optional[OrderTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class PageSortType:
    class Meta:
        name = "pageSortType"

    value: Optional[PageSortTypeEnum] = field(
        default=None,
    )
    order: Optional[OrderTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class RangeFacetResultItem(FacetResultItem):
    class Meta:
        name = "rangeFacetResultItem"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class RangeMatcherType:
    class Meta:
        name = "rangeMatcherType"

    inclusive_end: Optional[bool] = field(
        default=None,
        metadata={
            "name": "inclusiveEnd",
            "type": "Attribute",
        }
    )
    match: Optional[Match] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class RedirectList:
    class Meta:
        name = "redirectList"

    entry: List[RedirectEntry] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    last_update: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "lastUpdate",
            "type": "Attribute",
        }
    )


@dataclass
class ResultType:
    class Meta:
        name = "resultType"

    items: Optional["ResultType.Items"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    total: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    total_qualifier: Optional[TotalQualifier] = field(
        default=None,
        metadata={
            "name": "totalQualifier",
            "type": "Attribute",
        }
    )
    offset: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    max: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

    @dataclass
    class Items:
        item: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:vpro:api:2013",
            }
        )


@dataclass
class ScheduleEventApiType(ScheduleEventType):
    class Meta:
        name = "scheduleEventApiType"

    program: Optional[Program] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    group: Optional[Group] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    segment: Optional[Segment] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )


@dataclass
class SearchResultItem:
    class Meta:
        name = "searchResultItem"

    result: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    highlight: List[HightlightType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    score: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class SimpleMatcherType:
    class Meta:
        name = "simpleMatcherType"

    value: Optional[str] = field(
        default=None,
    )
    fuzziness: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    match_type: Optional[SimpleMatchType] = field(
        default=None,
        metadata={
            "name": "matchType",
            "type": "Attribute",
        }
    )
    match: Optional[Match] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TermFacetResultItemType(FacetResultItem):
    class Meta:
        name = "termFacetResultItemType"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class TextFacetType(AbstractFacetType):
    class Meta:
        name = "textFacetType"

    threshold: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    max: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    include: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    script: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    sort: Optional[FacetOrderTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TextMatcherType:
    class Meta:
        name = "textMatcherType"

    value: Optional[str] = field(
        default=None,
    )
    match_type: Optional[StandardMatchType] = field(
        default=None,
        metadata={
            "name": "matchType",
            "type": "Attribute",
        }
    )
    match: Optional[Match] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TitleSearchType:
    class Meta:
        name = "titleSearchType"

    value: Optional[str] = field(
        default=None,
    )
    owner: Optional[OwnerTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    type: Optional[TextualTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    match_type: Optional[StandardMatchType] = field(
        default=None,
        metadata={
            "name": "matchType",
            "type": "Attribute",
        }
    )
    match: Optional[Match] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class DateFacetResultItemType(RangeFacetResultItem):
    class Meta:
        name = "dateFacetResultItemType"

    begin: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    end: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class DateRangeMatcherType(RangeMatcherType):
    class Meta:
        name = "dateRangeMatcherType"

    begin: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    end: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class DurationFacetResultItemType(RangeFacetResultItem):
    class Meta:
        name = "durationFacetResultItemType"

    begin: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    end: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class DurationRangeMatcherType(RangeMatcherType):
    class Meta:
        name = "durationRangeMatcherType"

    begin: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    end: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class ExtendedTextMatcherListType(MatcherList):
    class Meta:
        name = "extendedTextMatcherListType"

    matcher: List[ExtendedMatcherType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class MediaGenreFacetResultItemType(TermFacetResultItemType):
    class Meta:
        name = "mediaGenreFacetResultItemType"

    term: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class MediaGeoLocationFacetResultItemType(TermFacetResultItemType):
    class Meta:
        name = "mediaGeoLocationFacetResultItemType"

    term: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class MediaTitleFacetType(TextFacetType):
    class Meta:
        name = "mediaTitleFacetType"

    sub_search: Optional[TitleSearchType] = field(
        default=None,
        metadata={
            "name": "subSearch",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


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


@dataclass
class NamedTermFacetResultItemType:
    class Meta:
        name = "namedTermFacetResultItemType"

    facet: List[TermFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class PageGenreFacetResultItemType(TermFacetResultItemType):
    class Meta:
        name = "pageGenreFacetResultItemType"

    term: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class PageSortListType:
    class Meta:
        name = "pageSortListType"

    sort: List[PageSortType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )


@dataclass
class Redirects(RedirectList):
    class Meta:
        name = "redirects"
        namespace = "urn:vpro:api:2013"


@dataclass
class ScheduleEventSearchType(RangeMatcherType):
    class Meta:
        name = "scheduleEventSearchType"

    begin: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    end: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    channel: Optional[ChannelEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    net: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    rerun: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class ScheduleItem(ScheduleEventApiType):
    class Meta:
        name = "scheduleItem"
        namespace = "urn:vpro:api:2013"


@dataclass
class SearchResultType(ResultType):
    class Meta:
        name = "searchResultType"


@dataclass
class TextMatcherListType(MatcherList):
    class Meta:
        name = "textMatcherListType"

    matcher: List[TextMatcherType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class TitleSortOrderType(MediaSortType):
    class Meta:
        name = "titleSortOrderType"

    type: Optional[TextualTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    owner: Optional[OwnerTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class AssociationSearchType:
    class Meta:
        name = "associationSearchType"

    urls: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
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


@dataclass
class DateRangeMatcherListType(MatcherList):
    class Meta:
        name = "dateRangeMatcherListType"

    matcher: List[DateRangeMatcherType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class DurationRangeMatcherListType(MatcherList):
    class Meta:
        name = "durationRangeMatcherListType"

    matcher: List[DurationRangeMatcherType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class MediaFacetsResultType:
    class Meta:
        name = "mediaFacetsResultType"

    titles: List[TermFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    types: List[TermFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    av_types: List[TermFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "name": "avTypes",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    sort_dates: List[DateFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "name": "sortDates",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    broadcasters: List[TermFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    genres: List[MediaGenreFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    geo_locations: List[MediaGeoLocationFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "name": "geoLocations",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    tags: List[TermFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    durations: List[DurationFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    descendant_of: List[MemberRefFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "name": "descendantOf",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    episode_of: List[MemberRefFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "name": "episodeOf",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    member_of: List[MemberRefFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "name": "memberOf",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    relations: List[NamedTermFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    age_ratings: List[TermFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "name": "ageRatings",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    content_ratings: List[TermFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "name": "contentRatings",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )


@dataclass
class MediaRelationSearchType:
    class Meta:
        name = "mediaRelationSearchType"

    types: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    broadcasters: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    values: Optional[ExtendedTextMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    uri_refs: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "name": "uriRefs",
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


@dataclass
class PageFacetsResultType:
    class Meta:
        name = "pageFacetsResultType"

    sort_dates: List[DateFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "name": "sortDates",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    types: List[TermFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    broadcasters: List[TermFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    tags: List[TermFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    keywords: List[TermFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    genres: List[PageGenreFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    portals: List[TermFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    sections: List[TermFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    relations: List[NamedTermFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )


@dataclass
class PageRelationSearchType:
    class Meta:
        name = "pageRelationSearchType"

    types: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    broadcasters: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    values: Optional[ExtendedTextMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    uri_refs: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "name": "uriRefs",
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


@dataclass
class SubtitlesSearchType:
    class Meta:
        name = "subtitlesSearchType"

    text: Optional[SimpleMatcherType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    mids: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
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
    languages: Optional[TextMatcherListType] = field(
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


@dataclass
class TermSearchType:
    class Meta:
        name = "termSearchType"

    ids: Optional[TextMatcherListType] = field(
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


@dataclass
class GenericMediaSearchResultType(SearchResultType):
    class Meta:
        name = "genericMediaSearchResultType"

    facets: Optional[MediaFacetsResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    selected_facets: Optional[MediaFacetsResultType] = field(
        default=None,
        metadata={
            "name": "selectedFacets",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class MediaRelationSearchListType:
    class Meta:
        name = "mediaRelationSearchListType"

    relation_search: List[MediaRelationSearchType] = field(
        default_factory=list,
        metadata={
            "name": "relationSearch",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class PageAssociationSearchListType:
    class Meta:
        name = "pageAssociationSearchListType"

    search: List[AssociationSearchType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class PageRelationSearchListType:
    class Meta:
        name = "pageRelationSearchListType"

    relation_search: List[PageRelationSearchType] = field(
        default_factory=list,
        metadata={
            "name": "relationSearch",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class PageSearchResultType(SearchResultType):
    class Meta:
        name = "pageSearchResultType"

    facets: Optional[PageFacetsResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    selected_facets: Optional[PageFacetsResultType] = field(
        default=None,
        metadata={
            "name": "selectedFacets",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    media_facets: Optional[MediaFacetsResultType] = field(
        default=None,
        metadata={
            "name": "mediaFacets",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    media_selected_facets: Optional[MediaFacetsResultType] = field(
        default=None,
        metadata={
            "name": "mediaSelectedFacets",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class SubtitlesFormType:
    class Meta:
        name = "subtitlesFormType"

    searches: Optional[SubtitlesSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class MediaSearchResultType(GenericMediaSearchResultType):
    class Meta:
        name = "mediaSearchResultType"


@dataclass
class MediaSearchType:
    """
    Limits the search result to media with certain properties.
    """
    class Meta:
        name = "mediaSearchType"

    text: Optional[SimpleMatcherType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    media_ids: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "name": "mediaIds",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "doc": "The MID must match one of the mediaIds",
        }
    )
    types: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "doc": "The media type must match one of these.",
        }
    )
    av_types: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "name": "avTypes",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    sort_dates: Optional[DateRangeMatcherListType] = field(
        default=None,
        metadata={
            "name": "sortDates",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    publish_dates: Optional[DateRangeMatcherListType] = field(
        default=None,
        metadata={
            "name": "publishDates",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    creation_dates: Optional[DateRangeMatcherListType] = field(
        default=None,
        metadata={
            "name": "creationDates",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    last_modified_dates: Optional[DateRangeMatcherListType] = field(
        default=None,
        metadata={
            "name": "lastModifiedDates",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    broadcasters: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    locations: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    tags: Optional[ExtendedTextMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    genres: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    durations: Optional[DurationRangeMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    descendant_of: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "name": "descendantOf",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    episode_of: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "name": "episodeOf",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    member_of: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "name": "memberOf",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    relations: Optional[MediaRelationSearchListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    schedule_events: List[ScheduleEventSearchType] = field(
        default_factory=list,
        metadata={
            "name": "scheduleEvents",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    age_ratings: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "name": "ageRatings",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    content_ratings: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "name": "contentRatings",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    titles: List[TitleSearchType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    geo_locations: List[GeoLocationSearchType] = field(
        default_factory=list,
        metadata={
            "name": "geoLocations",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    match: Optional[Match] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class PageSearchResult(PageSearchResultType):
    class Meta:
        name = "pageSearchResult"
        namespace = "urn:vpro:api:2013"


@dataclass
class PagesSearchType:
    class Meta:
        name = "pagesSearchType"

    text: Optional[SimpleMatcherType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    broadcasters: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
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
    portals: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    sections: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    genres: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    tags: Optional[ExtendedTextMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    keywords: Optional[ExtendedTextMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    sort_dates: Optional[DateRangeMatcherListType] = field(
        default=None,
        metadata={
            "name": "sortDates",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    last_modified_dates: Optional[DateRangeMatcherListType] = field(
        default=None,
        metadata={
            "name": "lastModifiedDates",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    creation_dates: Optional[DateRangeMatcherListType] = field(
        default=None,
        metadata={
            "name": "creationDates",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    publish_dates: Optional[DateRangeMatcherListType] = field(
        default=None,
        metadata={
            "name": "publishDates",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    relations: Optional[PageRelationSearchListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    links: Optional[PageAssociationSearchListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    referrals: Optional[PageAssociationSearchListType] = field(
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


@dataclass
class SubtitlesForm(SubtitlesFormType):
    class Meta:
        name = "subtitlesForm"
        namespace = "urn:vpro:api:2013"


@dataclass
class ExtendedMediaFacetType(TextFacetType):
    class Meta:
        name = "extendedMediaFacetType"

    filter: Optional[MediaSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    case_sensitive: Optional[bool] = field(
        default=None,
        metadata={
            "name": "caseSensitive",
            "type": "Attribute",
        }
    )


@dataclass
class ExtendedPageFacetType(TextFacetType):
    class Meta:
        name = "extendedPageFacetType"

    filter: Optional[PagesSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    case_sensitive: Optional[bool] = field(
        default=None,
        metadata={
            "name": "caseSensitive",
            "type": "Attribute",
        }
    )


@dataclass
class MediaFacetType(TextFacetType):
    class Meta:
        name = "mediaFacetType"

    filter: Optional[MediaSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class MediaSearchResult(MediaSearchResultType):
    class Meta:
        name = "mediaSearchResult"
        namespace = "urn:vpro:api:2013"


@dataclass
class PageFacetType(TextFacetType):
    class Meta:
        name = "pageFacetType"

    filter: Optional[PagesSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class ScheduleFormType:
    class Meta:
        name = "scheduleFormType"

    searches: Optional[MediaSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    highlight: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class MediaRelationFacetType(ExtendedMediaFacetType):
    class Meta:
        name = "mediaRelationFacetType"

    sub_search: Optional[MediaRelationSearchType] = field(
        default=None,
        metadata={
            "name": "subSearch",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class MediaSearchableTermFacetType(MediaFacetType):
    class Meta:
        name = "mediaSearchableTermFacetType"

    sub_search: Optional[TermSearchType] = field(
        default=None,
        metadata={
            "name": "subSearch",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class MediaTitleFacetListType(MediaFacetType):
    class Meta:
        name = "mediaTitleFacetListType"

    sub_search: Optional[TitleSearchType] = field(
        default=None,
        metadata={
            "name": "subSearch",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    title: List[MediaTitleFacetType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class MemberRefFacetType(MediaFacetType):
    class Meta:
        name = "memberRefFacetType"

    sub_search: Optional[MemberRefSearchType] = field(
        default=None,
        metadata={
            "name": "subSearch",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class PageRelationFacetType(ExtendedPageFacetType):
    class Meta:
        name = "pageRelationFacetType"

    sub_search: Optional[PageRelationSearchType] = field(
        default=None,
        metadata={
            "name": "subSearch",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class PageSearchableTermFacetType(PageFacetType):
    class Meta:
        name = "pageSearchableTermFacetType"

    sub_search: Optional[TermSearchType] = field(
        default=None,
        metadata={
            "name": "subSearch",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class ScheduleForm(ScheduleFormType):
    class Meta:
        name = "scheduleForm"
        namespace = "urn:vpro:api:2013"


@dataclass
class MediaRelationFacetListType(AbstractFacetType):
    class Meta:
        name = "mediaRelationFacetListType"

    filter: Optional[MediaSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    sub_search: Optional[MediaRelationSearchType] = field(
        default=None,
        metadata={
            "name": "subSearch",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    facet: List[MediaRelationFacetType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class PageRelationFacetListType(AbstractFacetType):
    class Meta:
        name = "pageRelationFacetListType"

    filter: Optional[PagesSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    sub_search: Optional[PageRelationSearchType] = field(
        default=None,
        metadata={
            "name": "subSearch",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    facet: List[PageRelationFacetType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class MediaFacetsType:
    class Meta:
        name = "mediaFacetsType"

    titles: Optional[MediaTitleFacetListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    types: Optional[MediaFacetType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    av_types: Optional[MediaFacetType] = field(
        default=None,
        metadata={
            "name": "avTypes",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    sort_dates: Optional[DateRangeFacetsType] = field(
        default=None,
        metadata={
            "name": "sortDates",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    broadcasters: Optional[MediaFacetType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    genres: Optional[MediaSearchableTermFacetType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    tags: Optional[ExtendedMediaFacetType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    durations: Optional[DurationRangeFacetsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    descendant_of: Optional[MemberRefFacetType] = field(
        default=None,
        metadata={
            "name": "descendantOf",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    episode_of: Optional[MemberRefFacetType] = field(
        default=None,
        metadata={
            "name": "episodeOf",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    member_of: Optional[MemberRefFacetType] = field(
        default=None,
        metadata={
            "name": "memberOf",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    relations: Optional[MediaRelationFacetListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    age_ratings: Optional[MediaFacetType] = field(
        default=None,
        metadata={
            "name": "ageRatings",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    content_ratings: Optional[MediaFacetType] = field(
        default=None,
        metadata={
            "name": "contentRatings",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    geo_locations: Optional[MediaSearchableTermFacetType] = field(
        default=None,
        metadata={
            "name": "geoLocations",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    filter: Optional[MediaSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class PagesFacetsType:
    class Meta:
        name = "pagesFacetsType"

    sort_dates: Optional[DateRangeFacetsType] = field(
        default=None,
        metadata={
            "name": "sortDates",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    broadcasters: Optional[PageFacetType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    types: Optional[PageFacetType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    tags: Optional[ExtendedPageFacetType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    keywords: Optional[ExtendedPageFacetType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    genres: Optional[PageSearchableTermFacetType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    portals: Optional[PageFacetType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    sections: Optional[PageFacetType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    relations: Optional[PageRelationFacetListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    filter: Optional[PagesSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class MediaFormType:
    class Meta:
        name = "mediaFormType"

    searches: Optional[MediaSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    sort_fields: Optional["MediaFormType.SortFields"] = field(
        default=None,
        metadata={
            "name": "sortFields",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    facets: Optional[MediaFacetsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    highlight: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

    @dataclass
    class SortFields:
        sort: List[MediaSortType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:vpro:api:2013",
                "sequential": True,
            }
        )
        title_sort: List[TitleSortOrderType] = field(
            default_factory=list,
            metadata={
                "name": "titleSort",
                "type": "Element",
                "namespace": "urn:vpro:api:2013",
                "sequential": True,
            }
        )


@dataclass
class MediaForm(MediaFormType):
    class Meta:
        name = "mediaForm"
        namespace = "urn:vpro:api:2013"


@dataclass
class PagesFormType:
    class Meta:
        name = "pagesFormType"

    searches: Optional[PagesSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    sort_fields: Optional[PageSortListType] = field(
        default=None,
        metadata={
            "name": "sortFields",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    facets: Optional[PagesFacetsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    media_form: Optional[MediaForm] = field(
        default=None,
        metadata={
            "name": "mediaForm",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    highlight: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class PagesForm(PagesFormType):
    class Meta:
        name = "pagesForm"
        namespace = "urn:vpro:api:2013"
