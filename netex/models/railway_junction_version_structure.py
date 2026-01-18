from __future__ import annotations

from dataclasses import dataclass

from .infrastructure_point_version_structure import (
    InfrastructurePointVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RailwayJunctionVersionStructure(InfrastructurePointVersionStructure):
    class Meta:
        name = "RailwayJunction_VersionStructure"
