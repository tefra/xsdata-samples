from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .mobility_service_constraint_zone import MobilityServiceConstraintZone
from .mobility_service_constraint_zone_ref import (
    MobilityServiceConstraintZoneRef,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MobilityServiceConstraintZonesRelStructure(
    ContainmentAggregationStructure
):
    class Meta:
        name = "mobilityServiceConstraintZones_RelStructure"

    mobility_service_constraint_zone_ref_or_mobility_service_constraint_zone: Iterable[
        MobilityServiceConstraintZoneRef | MobilityServiceConstraintZone
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "MobilityServiceConstraintZoneRef",
                    "type": MobilityServiceConstraintZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MobilityServiceConstraintZone",
                    "type": MobilityServiceConstraintZone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
