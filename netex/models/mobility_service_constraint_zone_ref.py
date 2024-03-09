from dataclasses import dataclass

from .mobility_service_constraint_zone_ref_structure import (
    MobilityServiceConstraintZoneRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MobilityServiceConstraintZoneRef(
    MobilityServiceConstraintZoneRefStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
