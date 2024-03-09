from dataclasses import dataclass

from .address_version_structure import AddressVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Address(AddressVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
