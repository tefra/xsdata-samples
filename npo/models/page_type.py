from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate, XmlDateTime

from npo.models.broadcaster_type import BroadcasterType
from npo.models.embed_type import EmbedType
from npo.models.genre import Genre
from npo.models.image_type_2 import ImageType2
from npo.models.link_type import LinkType
from npo.models.page_type_enum import PageTypeEnum
from npo.models.page_workflow import PageWorkflow
from npo.models.paragraph_type import ParagraphType
from npo.models.portal_type import PortalType
from npo.models.referral_type import ReferralType
from npo.models.relation_type_2 import RelationType2

__NAMESPACE__ = "urn:vpro:pages:2013"


@dataclass
class PageType:
    class Meta:
        name = "pageType"

    crid: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    alternative_url: list[str] = field(
        default_factory=list,
        metadata={
            "name": "alternativeUrl",
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    broadcaster: list[BroadcasterType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
            "min_occurs": 1,
        },
    )
    portal: None | PortalType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
            "required": True,
        },
    )
    sub_title: None | str = field(
        default=None,
        metadata={
            "name": "subTitle",
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    keyword: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    genre: list[Genre] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    summary: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    paragraphs: None | PageType.Paragraphs = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    tag: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    referral: list[ReferralType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    link: list[LinkType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    embed: list[EmbedType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    stat_ref: list[str] = field(
        default_factory=list,
        metadata={
            "name": "statRef",
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    images: None | PageType.Images = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    relation: list[RelationType2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    url: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    type_value: None | PageTypeEnum = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        },
    )
    creation_date: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "creationDate",
            "type": "Attribute",
        },
    )
    last_modified: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "lastModified",
            "type": "Attribute",
        },
    )
    last_published: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "lastPublished",
            "type": "Attribute",
        },
    )
    publish_start: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "publishStart",
            "type": "Attribute",
        },
    )
    publish_stop: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "publishStop",
            "type": "Attribute",
        },
    )
    ref_count: None | int = field(
        default=None,
        metadata={
            "name": "refCount",
            "type": "Attribute",
        },
    )
    sort_date: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "sortDate",
            "type": "Attribute",
        },
    )
    workflow: None | PageWorkflow = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class Paragraphs:
        paragraph: list[ParagraphType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:vpro:pages:2013",
            },
        )

    @dataclass
    class Images:
        image: list[ImageType2] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:vpro:pages:2013",
            },
        )
