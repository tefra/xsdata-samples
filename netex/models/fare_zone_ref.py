from dataclasses import dataclass

from .fare_zone_ref_structure import FareZoneRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareZoneRef(FareZoneRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
