from dataclasses import dataclass
from .postal_address_ref_structure import PostalAddressRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PostalAddressRef(PostalAddressRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
