from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlDuration

__NAMESPACE__ = "urn:vpro:shared:2009"


class ImageTypeEnum(Enum):
    PICTURE = "PICTURE"
    PORTRAIT = "PORTRAIT"
    STILL = "STILL"
    LOGO = "LOGO"
    ICON = "ICON"
    PROMO_LANDSCAPE = "PROMO_LANDSCAPE"
    PROMO_PORTRAIT = "PROMO_PORTRAIT"
    BACKGROUND = "BACKGROUND"


class LicenseEnum(Enum):
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
    """The type of a subtitles object.

    TODO these descriptions are provisional?
    """
    CAPTION = "CAPTION"
    TRANSLATION = "TRANSLATION"
    TRANSCRIPT = "TRANSCRIPT"


SubtitlesTypeEnum.CAPTION.__doc__ = (
    "The subtitles represent a textual version of what is spoken or wat is "
    "happening. They are expected to be in the same language as the video "
    "itself. Teletekst 888 subtitles are captions."
)
SubtitlesTypeEnum.TRANSLATION.__doc__ = (
    "The subtitles represent a translation. They are expected to be in a "
    "different language than the main language that can be heard"
)
SubtitlesTypeEnum.TRANSCRIPT.__doc__ = (
    "The subtitles represent a precise or automatic version of what is being "
    "said."
)


class SubtitlesWorkflowEnum(Enum):
    IGNORE = "IGNORE"
    REVOKED = "REVOKED"
    FOR_DELETION = "FOR_DELETION"
    DELETED = "DELETED"
    FOR_PUBLICATION = "FOR_PUBLICATION"
    FOR_REPUBLICATION = "FOR_REPUBLICATION"
    PUBLISHED = "PUBLISHED"
    PUBLISH_ERROR = "PUBLISH_ERROR"


class WorkflowEnumType(Enum):
    """These are the possible values of several 'workflow' fields.

    These serve administrative purposes only. In the Frontent API you
    should only encounter 'PUBLISHED'.
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


WorkflowEnumType.IGNORE.__doc__ = (
    "This means that the object is ignored for workflow changes. This is "
    "mainly usefull during testing."
)


@dataclass
class ImageType:
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
    offset: Optional[XmlDuration] = field(
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
    publish_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "publishDate",
            "type": "Attribute",
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
    workflow: Optional[WorkflowEnumType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class PublishableObjectType:
    class Meta:
        name = "publishableObjectType"

    urn: Optional[str] = field(
        default=None,
        metadata={
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
    publish_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "publishDate",
            "type": "Attribute",
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
