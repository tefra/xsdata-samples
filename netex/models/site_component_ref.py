from dataclasses import dataclass
from netex.models.site_component_ref_structure import SiteComponentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SiteComponentRef(SiteComponentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
