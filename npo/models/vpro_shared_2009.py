from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "urn:vpro:shared:2009"


class ImageTypeEnum(Enum):
    """
    :cvar PICTURE:
    :cvar PORTRAIT:
    :cvar STILL:
    :cvar LOGO:
    :cvar ICON:
    :cvar PROMO_LANDSCAPE:
    :cvar PROMO_PORTRAIT:
    :cvar BACKGROUND:
    """
    PICTURE = "PICTURE"
    PORTRAIT = "PORTRAIT"
    STILL = "STILL"
    LOGO = "LOGO"
    ICON = "ICON"
    PROMO_LANDSCAPE = "PROMO_LANDSCAPE"
    PROMO_PORTRAIT = "PROMO_PORTRAIT"
    BACKGROUND = "BACKGROUND"


class LicenseEnum(Enum):
    """
    :cvar COPYRIGHTED:
    :cvar PUBLIC_DOMAIN:
    :cvar CC_BY:
    :cvar CC_BY_1_0:
    :cvar CC_BY_2_0:
    :cvar CC_BY_3_0:
    :cvar CC_BY_4_0:
    :cvar CC_BY_SA:
    :cvar CC_BY_SA_1_0:
    :cvar CC_BY_SA_2_0:
    :cvar CC_BY_SA_3_0:
    :cvar CC_BY_SA_4_0:
    :cvar CC_BY_ND:
    :cvar CC_BY_ND_1_0:
    :cvar CC_BY_ND_2_0:
    :cvar CC_BY_ND_3_0:
    :cvar CC_BY_ND_4_0:
    :cvar CC_BY_NC:
    :cvar CC_BY_NC_1_0:
    :cvar CC_BY_NC_2_0:
    :cvar CC_BY_NC_3_0:
    :cvar CC_BY_NC_4_0:
    :cvar CC_BY_NC_SA:
    :cvar CC_BY_NC_SA_1_0:
    :cvar CC_BY_NC_SA_2_0:
    :cvar CC_BY_NC_SA_3_0:
    :cvar CC_BY_NC_SA_4_0:
    :cvar CC_BY_NC_ND:
    :cvar CC_BY_NC_ND_1_0:
    :cvar CC_BY_NC_ND_2_0:
    :cvar CC_BY_NC_ND_3_0:
    :cvar CC_BY_NC_ND_4_0:
    :cvar USA_GOV:
    """
    COPYRIGHTED = "COPYRIGHTED"
    PUBLIC_DOMAIN = "PUBLIC_DOMAIN"
    CC_BY = "CC_BY"
    CC_BY_1_0 = "CC_BY_1_0"
    CC_BY_2_0 = "CC_BY_2_0"
    CC_BY_3_0 = "CC_BY_3_0"
    CC_BY_4_0 = "CC_BY_4_0"
    CC_BY_SA = "CC_BY_SA"
    CC_BY_SA_1_0 = "CC_BY_SA_1_0"
    CC_BY_SA_2_0 = "CC_BY_SA_2_0"
    CC_BY_SA_3_0 = "CC_BY_SA_3_0"
    CC_BY_SA_4_0 = "CC_BY_SA_4_0"
    CC_BY_ND = "CC_BY_ND"
    CC_BY_ND_1_0 = "CC_BY_ND_1_0"
    CC_BY_ND_2_0 = "CC_BY_ND_2_0"
    CC_BY_ND_3_0 = "CC_BY_ND_3_0"
    CC_BY_ND_4_0 = "CC_BY_ND_4_0"
    CC_BY_NC = "CC_BY_NC"
    CC_BY_NC_1_0 = "CC_BY_NC_1_0"
    CC_BY_NC_2_0 = "CC_BY_NC_2_0"
    CC_BY_NC_3_0 = "CC_BY_NC_3_0"
    CC_BY_NC_4_0 = "CC_BY_NC_4_0"
    CC_BY_NC_SA = "CC_BY_NC_SA"
    CC_BY_NC_SA_1_0 = "CC_BY_NC_SA_1_0"
    CC_BY_NC_SA_2_0 = "CC_BY_NC_SA_2_0"
    CC_BY_NC_SA_3_0 = "CC_BY_NC_SA_3_0"
    CC_BY_NC_SA_4_0 = "CC_BY_NC_SA_4_0"
    CC_BY_NC_ND = "CC_BY_NC_ND"
    CC_BY_NC_ND_1_0 = "CC_BY_NC_ND_1_0"
    CC_BY_NC_ND_2_0 = "CC_BY_NC_ND_2_0"
    CC_BY_NC_ND_3_0 = "CC_BY_NC_ND_3_0"
    CC_BY_NC_ND_4_0 = "CC_BY_NC_ND_4_0"
    USA_GOV = "USA_GOV"


class OwnerTypeEnum(Enum):
    """
    :cvar BROADCASTER:
    :cvar NEBO:
    :cvar NPO:
    :cvar MIS:
    :cvar CERES:
    :cvar PLUTO:
    :cvar PROJECTM:
    :cvar WHATS_ON:
    :cvar IMMIX:
    :cvar AUTHORITY:
    :cvar RADIOBOX:
    :cvar BEELDENGELUID:
    """
    BROADCASTER = "BROADCASTER"
    NEBO = "NEBO"
    NPO = "NPO"
    MIS = "MIS"
    CERES = "CERES"
    PLUTO = "PLUTO"
    PROJECTM = "PROJECTM"
    WHATS_ON = "WHATS_ON"
    IMMIX = "IMMIX"
    AUTHORITY = "AUTHORITY"
    RADIOBOX = "RADIOBOX"
    BEELDENGELUID = "BEELDENGELUID"


class SubtitlesTypeEnum(Enum):
    """The type of a subtitles object. TODO these descriptions are provisional?

    :cvar CAPTION: The subtitles represent a textual version of what is spoken or wat is happening. They are expected to be in the same language as the video itself. Teletekst 888 subtitles are captions.
    :cvar TRANSLATION: The subtitles represent a translation. They are expected to be in a different language than the main language that can be heard
    :cvar TRANSCRIPT: The subtitles represent a precise or automatic version of what is being said.
    """
    CAPTION = "CAPTION"
    TRANSLATION = "TRANSLATION"
    TRANSCRIPT = "TRANSCRIPT"


class SubtitlesWorkflowEnum(Enum):
    """
    :cvar IGNORE:
    :cvar REVOKED:
    :cvar FOR_DELETION:
    :cvar DELETED:
    :cvar FOR_PUBLICATION:
    :cvar FOR_REPUBLICATION:
    :cvar PUBLISHED:
    :cvar PUBLISH_ERROR:
    """
    IGNORE = "IGNORE"
    REVOKED = "REVOKED"
    FOR_DELETION = "FOR_DELETION"
    DELETED = "DELETED"
    FOR_PUBLICATION = "FOR_PUBLICATION"
    FOR_REPUBLICATION = "FOR_REPUBLICATION"
    PUBLISHED = "PUBLISHED"
    PUBLISH_ERROR = "PUBLISH_ERROR"


class WorkflowEnumType(Enum):
    """These are the possible values of several 'workflow' fields. These serve
    administrative purposes only. In the Frontent API you should only encounter
    'PUBLISHED'.

    :cvar FOR_PUBLICATION:
    :cvar FOR_REPUBLICATION:
    :cvar PUBLISHED:
    :cvar PARENT_REVOKED:
    :cvar REVOKED:
    :cvar FOR_DELETION:
    :cvar DELETED:
    :cvar MERGED:
    :cvar IGNORE: This means that the object is ignored for workflow changes. This is mainly usefull during testing.
    """
    FOR_PUBLICATION = "FOR PUBLICATION"
    FOR_REPUBLICATION = "FOR REPUBLICATION"
    PUBLISHED = "PUBLISHED"
    PARENT_REVOKED = "PARENT REVOKED"
    REVOKED = "REVOKED"
    FOR_DELETION = "FOR DELETION"
    DELETED = "DELETED"
    MERGED = "MERGED"
    IGNORE = "IGNORE"


@dataclass
class ImageType:
    """
    :ivar title:
    :ivar description:
    :ivar image_uri:
    :ivar offset:
    :ivar height:
    :ivar width:
    :ivar credits:
    :ivar source:
    :ivar source_name:
    :ivar license:
    :ivar date:
    :ivar type:
    :ivar owner:
    :ivar highlighted:
    :ivar urn:
    :ivar publish_start:
    :ivar publish_stop:
    :ivar publish_date:
    :ivar creation_date:
    :ivar last_modified:
    :ivar workflow:
    """
    class Meta:
        name = "imageType"

    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
            "required": True,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
        }
    )
    image_uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "imageUri",
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
        }
    )
    offset: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
        }
    )
    height: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
        }
    )
    width: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
        }
    )
    credits: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
        }
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
        }
    )
    source_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "sourceName",
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
        }
    )
    license: Optional[LicenseEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
        }
    )
    date: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
        }
    )
    type: Optional[ImageTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    owner: Optional[OwnerTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    highlighted: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    urn: Optional[str] = field(
        default=None,
        metadata={
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
    publish_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "publishDate",
            "type": "Attribute",
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
    workflow: Optional[WorkflowEnumType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class PublishableObjectType:
    """
    :ivar urn:
    :ivar publish_start:
    :ivar publish_stop:
    :ivar publish_date:
    :ivar creation_date:
    :ivar last_modified:
    :ivar workflow:
    """
    class Meta:
        name = "publishableObjectType"

    urn: Optional[str] = field(
        default=None,
        metadata={
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
    publish_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "publishDate",
            "type": "Attribute",
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
    workflow: Optional[WorkflowEnumType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Image(ImageType):
    class Meta:
        name = "image"
        namespace = "urn:vpro:shared:2009"
