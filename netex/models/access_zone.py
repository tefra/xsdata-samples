from dataclasses import dataclass

from .access_zone_version_structure import AccessZoneVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessZone(AccessZoneVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
