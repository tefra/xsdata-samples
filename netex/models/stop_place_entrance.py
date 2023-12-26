from dataclasses import dataclass
from .stop_place_entrance_version_structure import (
    StopPlaceEntranceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StopPlaceEntrance(StopPlaceEntranceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
