from __future__ import annotations

from dataclasses import dataclass

from .mobility_service_constraint_zone_version_structure import (
    MobilityServiceConstraintZoneVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MobilityServiceConstraintZone(
    MobilityServiceConstraintZoneVersionStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
