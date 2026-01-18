from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime, XmlDuration

from .data_objects_rel_structure import DataObjectsRelStructure
from .multilingual_string import MultilingualString
from .participant_ref import ParticipantRef
from .publication_request_structure import PublicationRequestStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PublicationDeliveryStructure:
    publication_timestamp: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "PublicationTimestamp",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    participant_ref: ParticipantRef | None = field(
        default=None,
        metadata={
            "name": "ParticipantRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    publication_request: PublicationRequestStructure | None = field(
        default=None,
        metadata={
            "name": "PublicationRequest",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    publication_refresh_interval: XmlDuration | None = field(
        default=None,
        metadata={
            "name": "PublicationRefreshInterval",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    data_objects: DataObjectsRelStructure | None = field(
        default=None,
        metadata={
            "name": "dataObjects",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    version: str = field(
        default="1.0",
        metadata={
            "type": "Attribute",
        },
    )
