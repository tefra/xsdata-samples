from dataclasses import dataclass
from netex.models.stop_area_ref_structure import StopAreaRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StopAreaRef(StopAreaRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
