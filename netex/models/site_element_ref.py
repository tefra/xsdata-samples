from dataclasses import dataclass
from netex.models.site_element_ref_structure import SiteElementRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SiteElementRef(SiteElementRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
