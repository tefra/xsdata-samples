from __future__ import annotations

from dataclasses import dataclass

from .flexible_point_properties_ref_structure import (
    FlexiblePointPropertiesRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexiblePointPropertiesRef(FlexiblePointPropertiesRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
