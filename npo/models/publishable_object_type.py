from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate, XmlDateTime
from npo.models.workflow_enum_type import WorkflowEnumType

__NAMESPACE__ = "urn:vpro:shared:2009"


@dataclass
class PublishableObjectType:
    class Meta:
        name = "publishableObjectType"

    urn: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    publish_start: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "publishStart",
            "type": "Attribute",
        }
    )
    publish_stop: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "publishStop",
            "type": "Attribute",
        }
    )
    publish_date: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "publishDate",
            "type": "Attribute",
        }
    )
    creation_date: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "creationDate",
            "type": "Attribute",
        }
    )
    last_modified: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "lastModified",
            "type": "Attribute",
        }
    )
    workflow: None | WorkflowEnumType = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
