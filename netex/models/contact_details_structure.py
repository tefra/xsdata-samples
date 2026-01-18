from dataclasses import dataclass, field
from typing import Optional

from .multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ContactDetailsStructure:
    contact_person: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "ContactPerson",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    email: str | None = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    phone: str | None = field(
        default=None,
        metadata={
            "name": "Phone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fax: str | None = field(
        default=None,
        metadata={
            "name": "Fax",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    url: str | None = field(
        default=None,
        metadata={
            "name": "Url",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    further_details: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "FurtherDetails",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
