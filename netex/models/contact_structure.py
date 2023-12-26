from dataclasses import dataclass, field
from typing import Optional
from .multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ContactStructure:
    contact_person: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ContactPerson",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    phone: Optional[str] = field(
        default=None,
        metadata={
            "name": "Phone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fax: Optional[str] = field(
        default=None,
        metadata={
            "name": "Fax",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "Url",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    further_details: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "FurtherDetails",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
