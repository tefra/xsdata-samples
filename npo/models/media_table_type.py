from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from npo.models.group_table_type import GroupTableType
from npo.models.location_table_type import LocationTableType
from npo.models.program_table_type import ProgramTableType
from npo.models.schedule import Schedule

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class MediaTableType:
    class Meta:
        name = "mediaTableType"

    program_table: None | ProgramTableType = field(
        default=None,
        metadata={
            "name": "programTable",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "doc": "A table with all program objects in this container",
        },
    )
    group_table: None | GroupTableType = field(
        default=None,
        metadata={
            "name": "groupTable",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "doc": "A table with all group objects in this container",
        },
    )
    location_table: None | LocationTableType = field(
        default=None,
        metadata={
            "name": "locationTable",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        },
    )
    schedule: None | Schedule = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "doc": "A table with all schedule information in this container",
        },
    )
    publisher: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    publication_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "publicationTime",
            "type": "Attribute",
        },
    )
    version: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
