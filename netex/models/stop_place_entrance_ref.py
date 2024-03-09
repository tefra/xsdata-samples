from dataclasses import dataclass

from .stop_place_entrance_ref_structure import StopPlaceEntranceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StopPlaceEntranceRef(StopPlaceEntranceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
