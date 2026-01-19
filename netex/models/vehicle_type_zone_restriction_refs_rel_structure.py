from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .vehicle_type_zone_restriction_ref import VehicleTypeZoneRestrictionRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleTypeZoneRestrictionRefsRelStructure(
    OneToManyRelationshipStructure
):
    class Meta:
        name = "vehicleTypeZoneRestrictionRefs_RelStructure"

    vehicle_type_zone_restriction_ref: Sequence[
        VehicleTypeZoneRestrictionRef
    ] = field(
        default_factory=list,
        metadata={
            "name": "VehicleTypeZoneRestrictionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
