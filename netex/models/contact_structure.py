from dataclasses import dataclass, field
from typing import Optional

from .contact_details_structure import ContactDetailsStructure
from .contact_ref import ContactRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ContactStructure(ContactDetailsStructure):
    contact_ref: ContactRef | None = field(
        default=None,
        metadata={
            "name": "ContactRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
