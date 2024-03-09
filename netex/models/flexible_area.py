from dataclasses import dataclass

from .flexible_area_version_structure import FlexibleAreaVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FlexibleArea(FlexibleAreaVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
