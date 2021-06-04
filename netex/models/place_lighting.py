from dataclasses import dataclass
from netex.models.place_lighting_version_structure import PlaceLightingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PlaceLighting(PlaceLightingVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
