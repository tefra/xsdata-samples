from dataclasses import dataclass

from .flexible_service_properties_ref_structure import (
    FlexibleServicePropertiesRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FlexibleServicePropertiesRef(FlexibleServicePropertiesRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
