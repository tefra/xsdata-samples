from __future__ import annotations

from dataclasses import dataclass, field

from .contact_details_structure import ContactDetailsStructure
from .contact_ref import ContactRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ContactStructure(ContactDetailsStructure):
    contact_ref: None | ContactRef = field(
        default=None,
        metadata={
            "name": "ContactRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
