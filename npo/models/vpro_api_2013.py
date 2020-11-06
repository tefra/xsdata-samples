from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
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
    """
    :ivar name:
    :ivar begin:
    :ivar end:
    """
    class Meta:
        name = "dateRangeFacetItemType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    begin: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    end: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


class DateRangePresetTypeEnum(Enum):
    """
    :cvar BEFORE_LAST_YEAR:
    :cvar LAST_YEAR:
    :cvar LAST_MONTH:
    :cvar LAST_WEEK:
    :cvar YESTERDAY:
    :cvar TODAY:
    :cvar THIS_WEEK:
    :cvar TOMORROW:
    """
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
    """
    :ivar name:
    :ivar begin:
    :ivar end:
    """
    class Meta:
        name = "durationRangeFacetItemType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    begin: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    end: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


class FacetOrderTypeEnum(Enum):
    """
    :cvar VALUE_ASC:
    :cvar VALUE_DESC:
    :cvar COUNT_ASC:
    :cvar COUNT_DESC:
    :cvar TERM:
    :cvar REVERSE_TERM:
    :cvar COUNT:
    :cvar REVERSE_COUNT:
    """
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
    """
    :ivar count:
    :ivar selected:
    """
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
    """
    :ivar body:
    :ivar term:
    """
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
    """
    :cvar MUST:
    :cvar SHOULD:
    :cvar NOT_VALUE:
    """
    MUST = "MUST"
    SHOULD = "SHOULD"
    NOT_VALUE = "NOT"


@dataclass
class MediaSearchResults:
    class Meta:
        name = "mediaSearchResults"


class MediaSortTypeEnum(Enum):
    """
    :cvar TITLE:
    :cvar SORT_DATE:
    :cvar PUBLISH_DATE:
    :cvar EPISODE:
    :cvar EPISODE_ADDED:
    :cvar MEMBER_ADDED:
    :cvar MEMBER:
    :cvar CREATION_DATE:
    :cvar LAST_MODIFIED:
    """
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
    """
    :cvar ASC:
    :cvar DESC:
    """
    ASC = "ASC"
    DESC = "DESC"


@dataclass
class PageSearchResults:
    class Meta:
        name = "pageSearchResults"


class PageSortTypeEnum(Enum):
    """
    :cvar SORT_DATE:
    :cvar LAST_MODIFIED:
    :cvar LAST_PUBLISHED:
    :cvar CREATION_DATE:
    """
    SORT_DATE = "sortDate"
    LAST_MODIFIED = "lastModified"
    LAST_PUBLISHED = "lastPublished"
    CREATION_DATE = "creationDate"


@dataclass
class RedirectEntry:
    """
    :ivar from_value:
    :ivar to:
    :ivar ultimate:
    :ivar circular:
    """
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
    """
    :cvar TEXT:
    """
    TEXT = "TEXT"


class StandardMatchType(Enum):
    """
    :cvar TEXT:
    :cvar REGEX:
    :cvar WILDCARD:
    """
    TEXT = "TEXT"
    REGEX = "REGEX"
    WILDCARD = "WILDCARD"


@dataclass
class Suggestion:
    """
    :ivar value:
    """
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
    """
    :cvar EQUAL_TO:
    :cvar APPROXIMATE:
    :cvar GREATER_THAN_OR_EQUAL_TO:
    :cvar MISSING:
    """
    EQUAL_TO = "EQUAL_TO"
    APPROXIMATE = "APPROXIMATE"
    GREATER_THAN_OR_EQUAL_TO = "GREATER_THAN_OR_EQUAL_TO"
    MISSING = "MISSING"


@dataclass
class DateRangeFacetsType(AbstractFacetType):
    """
    :ivar interval:
    :ivar preset:
    :ivar range:
    """
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
    """
    :ivar interval:
    :ivar range:
    """
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
    """
    :ivar value:
    :ivar fuzziness:
    :ivar match_type:
    :ivar case_sensitive:
    :ivar match:
    """
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
    """
    :ivar value:
    :ivar owner:
    :ivar role:
    :ivar gtaa_uri:
    :ivar match:
    """
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
    """
    :ivar match:
    """
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
    """
    :ivar value:
    :ivar order:
    """
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
    """
    :ivar value:
    :ivar order:
    """
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
    """
    :ivar value:
    """
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
    """
    :ivar inclusive_end:
    :ivar match:
    """
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
    """
    :ivar entry:
    :ivar last_update:
    """
    class Meta:
        name = "redirectList"

    entry: List[RedirectEntry] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    last_update: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastUpdate",
            "type": "Attribute",
        }
    )


@dataclass
class ResultType:
    """
    :ivar items:
    :ivar total:
    :ivar total_qualifier:
    :ivar offset:
    :ivar max:
    """
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
        """
        :ivar item:
        """
        item: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:vpro:api:2013",
            }
        )


@dataclass
class ScheduleEventApiType(ScheduleEventType):
    """
    :ivar program:
    :ivar group:
    :ivar segment:
    """
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
    """
    :ivar result:
    :ivar highlight:
    :ivar score:
    """
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
    """
    :ivar value:
    :ivar fuzziness:
    :ivar match_type:
    :ivar match:
    """
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
    """
    :ivar id:
    :ivar value:
    """
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
    """
    :ivar threshold:
    :ivar max:
    :ivar include:
    :ivar script:
    :ivar sort:
    """
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
    """
    :ivar value:
    :ivar match_type:
    :ivar match:
    """
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
    """
    :ivar value:
    :ivar owner:
    :ivar type:
    :ivar match_type:
    :ivar match:
    """
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
    """
    :ivar begin:
    :ivar end:
    :ivar name:
    """
    class Meta:
        name = "dateFacetResultItemType"

    begin: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    end: Optional[str] = field(
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
    """
    :ivar begin:
    :ivar end:
    """
    class Meta:
        name = "dateRangeMatcherType"

    begin: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    end: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class DurationFacetResultItemType(RangeFacetResultItem):
    """
    :ivar begin:
    :ivar end:
    """
    class Meta:
        name = "durationFacetResultItemType"

    begin: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    end: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class DurationRangeMatcherType(RangeMatcherType):
    """
    :ivar begin:
    :ivar end:
    """
    class Meta:
        name = "durationRangeMatcherType"

    begin: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    end: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class ExtendedTextMatcherListType(MatcherList):
    """
    :ivar matcher:
    """
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
    """
    :ivar term:
    """
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
    """
    :ivar term:
    """
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
    """
    :ivar sub_search:
    :ivar name:
    """
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
    """
    :ivar type:
    """
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
    """
    :ivar facet:
    :ivar name:
    """
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
    """
    :ivar term:
    """
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
    """
    :ivar sort:
    """
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
    """
    :ivar begin:
    :ivar end:
    :ivar channel:
    :ivar net:
    :ivar rerun:
    """
    class Meta:
        name = "scheduleEventSearchType"

    begin: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    end: Optional[str] = field(
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
    """
    :ivar matcher:
    """
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
    """
    :ivar type:
    :ivar owner:
    """
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
    """
    :ivar urls:
    :ivar types:
    :ivar match:
    """
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
    """
    :ivar matcher:
    """
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
    """
    :ivar matcher:
    """
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
    """
    :ivar titles:
    :ivar types:
    :ivar av_types:
    :ivar sort_dates:
    :ivar broadcasters:
    :ivar genres:
    :ivar geo_locations:
    :ivar tags:
    :ivar durations:
    :ivar descendant_of:
    :ivar episode_of:
    :ivar member_of:
    :ivar relations:
    :ivar age_ratings:
    :ivar content_ratings:
    """
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
    """
    :ivar types:
    :ivar broadcasters:
    :ivar values:
    :ivar uri_refs:
    :ivar match:
    """
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
    """
    :ivar media_ids:
    :ivar types:
    :ivar match:
    """
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
    """
    :ivar sort_dates:
    :ivar types:
    :ivar broadcasters:
    :ivar tags:
    :ivar keywords:
    :ivar genres:
    :ivar portals:
    :ivar sections:
    :ivar relations:
    """
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
    """
    :ivar types:
    :ivar broadcasters:
    :ivar values:
    :ivar uri_refs:
    :ivar match:
    """
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
    """
    :ivar text:
    :ivar mids:
    :ivar types:
    :ivar languages:
    :ivar match:
    """
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
    """
    :ivar ids:
    :ivar match:
    """
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
    """
    :ivar facets:
    :ivar selected_facets:
    """
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
    """
    :ivar relation_search:
    """
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
    """
    :ivar search:
    """
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
    """
    :ivar relation_search:
    """
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
    """
    :ivar facets:
    :ivar selected_facets:
    :ivar media_facets:
    :ivar media_selected_facets:
    """
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
    """
    :ivar searches:
    """
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
    """Limits the search result to media with certain properties.

    :ivar text:
    :ivar media_ids: The MID must match one of the mediaIds
    :ivar types: The media type must match one of these.
    :ivar av_types:
    :ivar sort_dates:
    :ivar publish_dates:
    :ivar creation_dates:
    :ivar last_modified_dates:
    :ivar broadcasters:
    :ivar locations:
    :ivar tags:
    :ivar genres:
    :ivar durations:
    :ivar descendant_of:
    :ivar episode_of:
    :ivar member_of:
    :ivar relations:
    :ivar schedule_events:
    :ivar age_ratings:
    :ivar content_ratings:
    :ivar titles:
    :ivar geo_locations:
    :ivar match:
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
        }
    )
    types: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
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
    """
    :ivar text:
    :ivar broadcasters:
    :ivar types:
    :ivar portals:
    :ivar sections:
    :ivar genres:
    :ivar tags:
    :ivar keywords:
    :ivar sort_dates:
    :ivar last_modified_dates:
    :ivar creation_dates:
    :ivar publish_dates:
    :ivar relations:
    :ivar links:
    :ivar referrals:
    :ivar match:
    """
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
    """
    :ivar filter:
    :ivar case_sensitive:
    """
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
    """
    :ivar filter:
    :ivar case_sensitive:
    """
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
    """
    :ivar filter:
    """
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
    """
    :ivar filter:
    """
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
    """
    :ivar searches:
    :ivar highlight:
    """
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
    """
    :ivar sub_search:
    :ivar name:
    """
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
    """
    :ivar sub_search:
    """
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
    """
    :ivar sub_search:
    :ivar title:
    """
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
    """
    :ivar sub_search:
    """
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
    """
    :ivar sub_search:
    :ivar name:
    """
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
    """
    :ivar sub_search:
    """
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
    """
    :ivar filter:
    :ivar sub_search:
    :ivar facet:
    """
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
    """
    :ivar filter:
    :ivar sub_search:
    :ivar facet:
    """
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
    """
    :ivar titles:
    :ivar types:
    :ivar av_types:
    :ivar sort_dates:
    :ivar broadcasters:
    :ivar genres:
    :ivar tags:
    :ivar durations:
    :ivar descendant_of:
    :ivar episode_of:
    :ivar member_of:
    :ivar relations:
    :ivar age_ratings:
    :ivar content_ratings:
    :ivar geo_locations:
    :ivar filter:
    """
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
    """
    :ivar sort_dates:
    :ivar broadcasters:
    :ivar types:
    :ivar tags:
    :ivar keywords:
    :ivar genres:
    :ivar portals:
    :ivar sections:
    :ivar relations:
    :ivar filter:
    """
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
    """
    :ivar searches:
    :ivar sort_fields:
    :ivar facets:
    :ivar highlight:
    """
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
        """
        :ivar sort:
        :ivar title_sort:
        """
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
    """
    :ivar searches:
    :ivar sort_fields:
    :ivar facets:
    :ivar media_form:
    :ivar highlight:
    """
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
