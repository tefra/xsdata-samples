from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from npo.models.vpro_media_2009 import (
    BroadcasterType,
    Group,
    Program,
    Segment,
)
from npo.models.vpro_shared_2009 import (
    ImageTypeEnum,
    LicenseEnum,
)

__NAMESPACE__ = "urn:vpro:pages:2013"


@dataclass
class GenreType:
    """
    :ivar term:
    :ivar display_name:
    :ivar id:
    """
    class Meta:
        name = "genreType"

    term: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    display_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


class LinkTypeEnum(Enum):
    """
    :cvar TOP_STORY:
    """
    TOP_STORY = "TOP_STORY"


class PageTypeEnum(Enum):
    """
    :cvar ARTICLE:
    :cvar SPECIAL:
    :cvar HOME:
    :cvar OVERVIEW:
    :cvar PRODUCT:
    :cvar PLAYER:
    :cvar AUDIO:
    :cvar VIDEO:
    :cvar MIXED:
    :cvar PLAYLIST:
    :cvar MOVIE:
    :cvar SERIES:
    :cvar PERSON:
    :cvar SEARCH:
    """
    ARTICLE = "ARTICLE"
    SPECIAL = "SPECIAL"
    HOME = "HOME"
    OVERVIEW = "OVERVIEW"
    PRODUCT = "PRODUCT"
    PLAYER = "PLAYER"
    AUDIO = "AUDIO"
    VIDEO = "VIDEO"
    MIXED = "MIXED"
    PLAYLIST = "PLAYLIST"
    MOVIE = "MOVIE"
    SERIES = "SERIES"
    PERSON = "PERSON"
    SEARCH = "SEARCH"


class PageWorkflow(Enum):
    """
    :cvar PUBLISHED:
    :cvar DELETED:
    """
    PUBLISHED = "PUBLISHED"
    DELETED = "DELETED"


@dataclass
class RelationType:
    """
    :ivar value:
    :ivar uri_ref:
    :ivar broadcaster:
    :ivar type:
    """
    class Meta:
        name = "relationType"

    value: Optional[str] = field(
        default=None,
    )
    uri_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "uriRef",
            "type": "Attribute",
        }
    )
    broadcaster: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class SectionType:
    """
    :ivar value:
    :ivar path:
    """
    class Meta:
        name = "sectionType"

    value: Optional[str] = field(
        default=None,
    )
    path: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class EmbedType:
    """
    :ivar title:
    :ivar description:
    :ivar group:
    :ivar program:
    :ivar segment:
    """
    class Meta:
        name = "embedType"

    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    group: Optional[Group] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    program: Optional[Program] = field(
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
class Genre(GenreType):
    class Meta:
        name = "genre"
        namespace = "urn:vpro:pages:2013"


@dataclass
class ImageType:
    """
    :ivar title:
    :ivar description:
    :ivar credits:
    :ivar source:
    :ivar source_name:
    :ivar license:
    :ivar type:
    :ivar url:
    """
    class Meta:
        name = "imageType"

    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    credits: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    source_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "sourceName",
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    license: Optional[LicenseEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    type: Optional[ImageTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class LinkType:
    """
    :ivar text:
    :ivar page_ref:
    :ivar type:
    """
    class Meta:
        name = "linkType"

    text: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    page_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "pageRef",
            "type": "Attribute",
        }
    )
    type: Optional[LinkTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class PortalType:
    """
    :ivar name:
    :ivar section:
    :ivar id:
    :ivar url:
    """
    class Meta:
        name = "portalType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
            "required": True,
        }
    )
    section: Optional[SectionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ReferralType:
    """
    :ivar value:
    :ivar referrer:
    :ivar type:
    """
    class Meta:
        name = "referralType"

    value: Optional[str] = field(
        default=None,
    )
    referrer: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    type: Optional[LinkTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ParagraphType:
    """
    :ivar title:
    :ivar body:
    :ivar image:
    """
    class Meta:
        name = "paragraphType"

    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    body: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    image: Optional[ImageType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )


@dataclass
class PageType:
    """
    :ivar crid:
    :ivar alternative_url:
    :ivar broadcaster:
    :ivar portal:
    :ivar title:
    :ivar sub_title:
    :ivar keyword:
    :ivar genre:
    :ivar summary:
    :ivar paragraphs:
    :ivar tag:
    :ivar referral:
    :ivar link:
    :ivar embed:
    :ivar stat_ref:
    :ivar images:
    :ivar relation:
    :ivar url:
    :ivar type:
    :ivar creation_date:
    :ivar last_modified:
    :ivar last_published:
    :ivar publish_start:
    :ivar publish_stop:
    :ivar ref_count:
    :ivar sort_date:
    :ivar workflow:
    """
    class Meta:
        name = "pageType"

    crid: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    alternative_url: List[str] = field(
        default_factory=list,
        metadata={
            "name": "alternativeUrl",
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    broadcaster: List[BroadcasterType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
            "min_occurs": 1,
        }
    )
    portal: Optional[PortalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
            "required": True,
        }
    )
    sub_title: Optional[str] = field(
        default=None,
        metadata={
            "name": "subTitle",
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    keyword: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    genre: List[Genre] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    summary: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    paragraphs: Optional["PageType.Paragraphs"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    tag: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    referral: List[ReferralType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    link: List[LinkType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    embed: List[EmbedType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    stat_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "statRef",
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    images: Optional["PageType.Images"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    relation: List[RelationType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    type: Optional[PageTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    creation_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "creationDate",
            "type": "Attribute",
        }
    )
    last_modified: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastModified",
            "type": "Attribute",
        }
    )
    last_published: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastPublished",
            "type": "Attribute",
        }
    )
    publish_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "publishStart",
            "type": "Attribute",
        }
    )
    publish_stop: Optional[str] = field(
        default=None,
        metadata={
            "name": "publishStop",
            "type": "Attribute",
        }
    )
    ref_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "refCount",
            "type": "Attribute",
        }
    )
    sort_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "sortDate",
            "type": "Attribute",
        }
    )
    workflow: Optional[PageWorkflow] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

    @dataclass
    class Paragraphs:
        """
        :ivar paragraph:
        """
        paragraph: List[ParagraphType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:vpro:pages:2013",
            }
        )

    @dataclass
    class Images:
        """
        :ivar image:
        """
        image: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:vpro:pages:2013",
            }
        )


@dataclass
class Page(PageType):
    class Meta:
        name = "page"
        namespace = "urn:vpro:pages:2013"
