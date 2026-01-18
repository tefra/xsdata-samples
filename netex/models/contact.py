from __future__ import annotations

from dataclasses import dataclass

from .contact_version_structure import ContactVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Contact(ContactVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
