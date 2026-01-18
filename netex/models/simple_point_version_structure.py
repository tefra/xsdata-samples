from dataclasses import dataclass, field

from .entity_in_version_structure import EntityInVersionStructure
from .location_structure_2 import LocationStructure2
from .multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SimplePointVersionStructure(EntityInVersionStructure):
    class Meta:
        name = "SimplePoint_VersionStructure"

    name: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    location: LocationStructure2 | None = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
