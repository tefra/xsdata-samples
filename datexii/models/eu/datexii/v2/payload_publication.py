from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.international_identifier import InternationalIdentifier
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class PayloadPublication:
    """
    A payload publication of traffic related information or associated management
    information created at a specific point in time that can be exchanged via a
    DATEX II interface.

    :ivar feed_description: A description of the information which is to
        be found in the publications originating from the particular
        feed (URL).
    :ivar feed_type: A classification of the information which is to be
        found in the publications originating from the particular feed.
    :ivar publication_time: Date/time at which the payload publication
        was created.
    :ivar publication_creator:
    :ivar payload_publication_extension:
    :ivar lang: The default language used throughout the payload
        publication.
    """
    feed_description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "feedDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    feed_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "feedType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    publication_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "publicationTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    publication_creator: Optional[InternationalIdentifier] = field(
        default=None,
        metadata={
            "name": "publicationCreator",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    payload_publication_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "payloadPublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
