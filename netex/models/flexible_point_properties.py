from dataclasses import dataclass
from .flexible_point_properties_versioned_child_structure import (
    FlexiblePointPropertiesVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FlexiblePointProperties(FlexiblePointPropertiesVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
