from dataclasses import dataclass
from netex.models.zone_version_structure import ZoneVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AdministrativeZone1(ZoneVersionStructure):
    class Meta:
        name = "AdministrativeZone_"
        namespace = "http://www.netex.org.uk/netex"
