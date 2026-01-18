from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime, XmlDuration

from npo.models.av_attributes_type import AvAttributesType
from npo.models.location_type_enum import LocationTypeEnum
from npo.models.owner_type_enum import OwnerTypeEnum
from npo.models.platform_type_enum import PlatformTypeEnum
from npo.models.workflow_enum_type import WorkflowEnumType

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass(kw_only=True)
class LocationType:
    class Meta:
        name = "locationType"

    program_url: str = field(
        metadata={
            "name": "programUrl",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "required": True,
        }
    )
    av_attributes: None | AvAttributesType = field(
        default=None,
        metadata={
            "name": "avAttributes",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        },
    )
    subtitles: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        },
    )
    offset: None | XmlDuration = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        },
    )
    duration: None | XmlDuration = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        },
    )
    type_value: None | LocationTypeEnum = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    platform: None | PlatformTypeEnum = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    owner: OwnerTypeEnum = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    urn: None | str = field(
        default=None,
        metadata={
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
    publish_date: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "publishDate",
            "type": "Attribute",
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
    workflow: None | WorkflowEnumType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
