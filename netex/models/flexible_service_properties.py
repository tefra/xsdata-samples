from __future__ import annotations

from dataclasses import dataclass

from .flexible_service_properties_version_structure import (
    FlexibleServicePropertiesVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexibleServiceProperties(FlexibleServicePropertiesVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
