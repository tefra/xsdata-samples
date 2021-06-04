from dataclasses import dataclass
from netex.models.site_component_version_structure import SiteComponentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointOfInterestComponentVersionStructure(SiteComponentVersionStructure):
    class Meta:
        name = "PointOfInterestComponent_VersionStructure"
