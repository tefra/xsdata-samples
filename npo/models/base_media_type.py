from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime, XmlDuration
from npo.models.age_rating_type import AgeRatingType
from npo.models.av_attributes_type import AvAttributesType
from npo.models.av_type_enum import AvTypeEnum
from npo.models.available_subtitle_type import AvailableSubtitleType
from npo.models.broadcaster_type import BroadcasterType
from npo.models.content_rating_type import ContentRatingType
from npo.models.country_type import CountryType
from npo.models.credits_type import CreditsType
from npo.models.descendant_ref_type import DescendantRefType
from npo.models.description_type import DescriptionType
from npo.models.genre_type_1 import GenreType1
from npo.models.geo_locations_type import GeoLocationsType
from npo.models.geo_restriction_type import GeoRestrictionType
from npo.models.images_type import ImagesType
from npo.models.intention_type import IntentionType
from npo.models.language_type import LanguageType
from npo.models.locations_type import LocationsType
from npo.models.member_ref_type import MemberRefType
from npo.models.organization_type import OrganizationType
from npo.models.portal_restriction_type import PortalRestrictionType
from npo.models.prediction_type import PredictionType
from npo.models.relation_type_1 import RelationType1
from npo.models.tag_type import TagType
from npo.models.target_groups_type import TargetGroupsType
from npo.models.title_type import TitleType
from npo.models.topics_type import TopicsType
from npo.models.twitter_type import TwitterType
from npo.models.workflow_enum_type import WorkflowEnumType

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class BaseMediaType:
    """This is the abstract base entity for programs, groups and segments.

    Actually these objects are very similar and share most properties.
    """
    class Meta:
        name = "baseMediaType"

    crid: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "doc": (
                "A crid (content reference identifier) is a reference to an "
                "entity in another system. E.g. a crid "
                "like\ncrid://broadcast.radiobox2/335793 refers to a broadcast"
                " with id 335793 in Radiobox. A crid must be a valid\nURI "
                "starting with \"crid://\". Crids must be unique, but they can"
                " be made up freely. It is a good idea to use\na logical "
                "structure which can easily be associated with another system."
                " Any POMS object can have zero or\nmore crids. They can refer"
                " to different systems, but a POMS object could also actually "
                "represent more than\none entity in a remote system."
            ),
        }
    )
    broadcaster: List[BroadcasterType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "min_occurs": 1,
            "doc": (
                "One or more broadcasters can be the owner of a POMS media "
                "object. This information is meta information about the "
                "object, but it is also used\nfor assigning write access to "
                "the object in the POMS backend to employees of these given "
                "broadcasting companies."
            ),
        }
    )
    portal: List[OrganizationType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "doc": (
                "Optionally 'portals' can be assigned to a media object. "
                "Portals are also 'owners', and employees can also work for a "
                "certain portal.\nThis is because some portal are shared by "
                "several broadcasting companies."
            ),
        }
    )
    exclusive: List[PortalRestrictionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "doc": (
                "Besides having portals, which mainly indicates where the "
                "object originates, a media object can also be assigned "
                "'portal restrictions'.\nIf a media object has any portal "
                "restrictions the media object may only be shown on these "
                "portals."
            ),
        }
    )
    region: List[GeoRestrictionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "doc": (
                "Media with a geo restriction can only be played in the "
                "indicated region (NL, BENELUX, WORLD). This\nrestriction "
                "doesn't apply to the metadata of the media object. It only "
                "applies to the actual playable content."
            ),
        }
    )
    title: List[TitleType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "min_occurs": 1,
            "doc": (
                "A media object has one or more titles. All titles have a type"
                " (MAIN, SUB etc.) and an owner (BROADCASTER, MIS etc.).\nThe "
                "combination of type and owner is always unique for a "
                "particular media object, so a media object cannot\nhave "
                "multiple titles of the same type and owner. Titles are sorted"
                " in order of the textualTypeEnum and the in order\nof "
                "ownerTypeEnum when published, so the first title in a "
                "published document will be a title owned by BROADCASTER of "
                "type\nMAIN, if that title exists."
            ),
        }
    )
    description: List[DescriptionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "doc": (
                "Optional descriptions for the media object. Descriptions have"
                " an owner and a type, and are ordered just like titles."
            ),
        }
    )
    genre: List[GenreType1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    tag: List[TagType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    intentions: List[IntentionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    target_groups: List[TargetGroupsType] = field(
        default_factory=list,
        metadata={
            "name": "targetGroups",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    geo_locations: List[GeoLocationsType] = field(
        default_factory=list,
        metadata={
            "name": "geoLocations",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    topics: List[TopicsType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    country: List[CountryType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    language: List[LanguageType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    is_dubbed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isDubbed",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    available_subtitles: List[AvailableSubtitleType] = field(
        default_factory=list,
        metadata={
            "name": "availableSubtitles",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    av_attributes: Optional[AvAttributesType] = field(
        default=None,
        metadata={
            "name": "avAttributes",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    release_year: Optional[int] = field(
        default=None,
        metadata={
            "name": "releaseYear",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    credits: Optional[CreditsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    award: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    descendant_of: List[DescendantRefType] = field(
        default_factory=list,
        metadata={
            "name": "descendantOf",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    member_of: List[MemberRefType] = field(
        default_factory=list,
        metadata={
            "name": "memberOf",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    age_rating: Optional[AgeRatingType] = field(
        default=None,
        metadata={
            "name": "ageRating",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    content_rating: List[ContentRatingType] = field(
        default_factory=list,
        metadata={
            "name": "contentRating",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    email: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    website: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "min_length": 1,
            "max_length": 255,
        }
    )
    twitter: List[TwitterType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    teletext: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    prediction: List[PredictionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    locations: Optional[LocationsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    relation: List[RelationType1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    images: Optional[ImagesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    mid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_length": 4,
            "max_length": 255,
            "pattern": r"[ \.a-zA-Z0-9_-]+",
        }
    )
    av_type: Optional[AvTypeEnum] = field(
        default=None,
        metadata={
            "name": "avType",
            "type": "Attribute",
            "required": True,
        }
    )
    sort_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "sortDate",
            "type": "Attribute",
        }
    )
    embeddable: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    has_subtitles: bool = field(
        default=False,
        metadata={
            "name": "hasSubtitles",
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
    merged_to: Optional[str] = field(
        default=None,
        metadata={
            "name": "mergedTo",
            "type": "Attribute",
            "min_length": 4,
            "max_length": 255,
            "pattern": r"[ \.a-zA-Z0-9_-]+",
        }
    )
