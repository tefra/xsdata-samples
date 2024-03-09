from dataclasses import dataclass

from .flexible_link_properties_versioned_child_structure import (
    FlexibleLinkPropertiesVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FlexibleLinkProperties(FlexibleLinkPropertiesVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
