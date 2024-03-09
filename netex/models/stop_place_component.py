from dataclasses import dataclass

from .stop_place_component_version_structure import (
    StopPlaceComponentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StopPlaceComponent(StopPlaceComponentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
