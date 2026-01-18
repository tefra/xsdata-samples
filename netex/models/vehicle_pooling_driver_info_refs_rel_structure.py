from __future__ import annotations

from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .vehicle_pooling_driver_info_ref import VehiclePoolingDriverInfoRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehiclePoolingDriverInfoRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "vehiclePoolingDriverInfoRefs_RelStructure"

    vehicle_pooling_driver_info_ref: None | VehiclePoolingDriverInfoRef = (
        field(
            default=None,
            metadata={
                "name": "VehiclePoolingDriverInfoRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "required": True,
            },
        )
    )
