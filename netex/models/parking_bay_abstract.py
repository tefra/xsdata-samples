from dataclasses import dataclass

from .site_component_version_structure import SiteComponentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingBayAbstract(SiteComponentVersionStructure):
    class Meta:
        name = "ParkingBay_"
        namespace = "http://www.netex.org.uk/netex"
