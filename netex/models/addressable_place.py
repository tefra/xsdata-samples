from dataclasses import dataclass
from .addressable_place_version_structure import (
    AddressablePlaceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AddressablePlace(AddressablePlaceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
