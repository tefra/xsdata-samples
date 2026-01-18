from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .vehicle_type_zone_restriction import VehicleTypeZoneRestriction

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleTypeZoneRestrictionsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "vehicleTypeZoneRestrictions_RelStructure"

    vehicle_type_zone_restriction: Iterable[VehicleTypeZoneRestriction] = (
        field(
            default_factory=list,
            metadata={
                "name": "VehicleTypeZoneRestriction",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
