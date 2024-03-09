from dataclasses import dataclass

from .zone_version_structure import ZoneVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AdministrativeZone2(ZoneVersionStructure):
    class Meta:
        name = "AdministrativeZone_"
        namespace = "http://www.netex.org.uk/netex"
