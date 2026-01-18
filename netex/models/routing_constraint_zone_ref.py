from __future__ import annotations

from dataclasses import dataclass

from .routing_constraint_zone_ref_structure import (
    RoutingConstraintZoneRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoutingConstraintZoneRef(RoutingConstraintZoneRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
