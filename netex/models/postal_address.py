from dataclasses import dataclass
from netex.models.postal_address_version_structure import PostalAddressVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PostalAddress(PostalAddressVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
