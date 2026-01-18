from __future__ import annotations

from dataclasses import dataclass

from .mobility_service_constraint_zone_ref_structure import (
    MobilityServiceConstraintZoneRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MobilityServiceConstraintZoneRef(
    MobilityServiceConstraintZoneRefStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
