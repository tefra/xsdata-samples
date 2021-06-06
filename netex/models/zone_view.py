from dataclasses import dataclass
from .zone_derived_view_structure import ZoneDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ZoneView(ZoneDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
