from dataclasses import dataclass
from netex.models.access_zone_ref_structure import AccessZoneRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessZoneRef(AccessZoneRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
