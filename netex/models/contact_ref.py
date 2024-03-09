from dataclasses import dataclass

from .contact_ref_structure import ContactRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ContactRef(ContactRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
