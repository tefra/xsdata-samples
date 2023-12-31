from dataclasses import dataclass
from .mobility_service_constraint_zone_version_structure import (
    MobilityServiceConstraintZoneVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MobilityServiceConstraintZone(
    MobilityServiceConstraintZoneVersionStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
