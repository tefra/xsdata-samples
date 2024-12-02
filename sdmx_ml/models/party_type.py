from dataclasses import dataclass, field
from typing import Optional

from sdmx_ml.models.contact_type_2 import ContactType2
from sdmx_ml.models.name import Name

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message"


@dataclass(frozen=True)
class PartyType:
    """
    PartyType defines the information which is sent about various parties such as
    senders and receivers of messages.

    :ivar name: Name is a human-readable name of the party.
    :ivar contact: Contact provides contact information for the party in
        regard to the transmission of the message.
    :ivar id: The id attribute holds the identification of the party.
    """

    name: tuple[Name, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common",
        },
    )
    contact: tuple[ContactType2, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Contact",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z0-9_@$\-]+",
        },
    )
