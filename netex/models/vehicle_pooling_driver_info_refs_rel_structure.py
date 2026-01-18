from __future__ import annotations

from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .vehicle_pooling_driver_info_ref import VehiclePoolingDriverInfoRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehiclePoolingDriverInfoRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "vehiclePoolingDriverInfoRefs_RelStructure"

    vehicle_pooling_driver_info_ref: VehiclePoolingDriverInfoRef = field(
        metadata={
            "name": "VehiclePoolingDriverInfoRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
