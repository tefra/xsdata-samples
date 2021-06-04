from dataclasses import dataclass
from netex.models.accommodation_versioned_child_structure import AccommodationVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Accommodation(AccommodationVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
