from dataclasses import dataclass
from netex.models.flexible_link_properties_ref_structure import FlexibleLinkPropertiesRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FlexibleLinkPropertiesRef(FlexibleLinkPropertiesRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
