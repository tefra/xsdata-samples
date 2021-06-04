from dataclasses import dataclass
from netex.models.address_ref_structure import AddressRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AddressRef(AddressRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
