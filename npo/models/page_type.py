from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
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
    relation: List[RelationType2] = field(
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
    creation_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "creationDate",
            "type": "Attribute",
        }
    )
    last_modified: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "lastModified",
            "type": "Attribute",
        }
    )
    last_published: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "lastPublished",
            "type": "Attribute",
        }
    )
    publish_start: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "publishStart",
            "type": "Attribute",
        }
    )
    publish_stop: Optional[XmlDateTime] = field(
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
    sort_date: Optional[XmlDateTime] = field(
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
        paragraph: List[ParagraphType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:vpro:pages:2013",
            }
        )

    @dataclass
    class Images:
        image: List[ImageType2] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:vpro:pages:2013",
            }
        )
