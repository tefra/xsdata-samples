from dataclasses import dataclass, field
from typing import Optional
from .entity_in_version_structure import EntityInVersionStructure
from .location_structure_2 import LocationStructure2
from .multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SimplePointVersionStructure(EntityInVersionStructure):
    class Meta:
        name = "SimplePoint_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    location: Optional[LocationStructure2] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
