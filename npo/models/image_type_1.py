from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlDuration
from npo.models.image_type_enum import ImageTypeEnum
from npo.models.license_enum import LicenseEnum
from npo.models.owner_type_enum import OwnerTypeEnum
from npo.models.workflow_enum_type import WorkflowEnumType

__NAMESPACE__ = "urn:vpro:shared:2009"


@dataclass
class ImageType1:
    class Meta:
        name = "imageType"

    title: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
            "required": True,
        },
    )
    description: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
        },
    )
    image_uri: None | str = field(
        default=None,
        metadata={
            "name": "imageUri",
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
        },
    )
    offset: None | XmlDuration = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
        },
    )
    height: None | int = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
        },
    )
    width: None | int = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
        },
    )
    credits: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
        },
    )
    source: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
        },
    )
    source_name: None | str = field(
        default=None,
        metadata={
            "name": "sourceName",
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
        },
    )
    license: None | LicenseEnum = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
        },
    )
    date: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
        },
    )
    type_value: None | ImageTypeEnum = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    owner: None | OwnerTypeEnum = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    highlighted: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
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
