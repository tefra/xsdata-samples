from dataclasses import dataclass, field
from typing import List

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .simple_vehicle_type_ref import SimpleVehicleTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SimpleVehicleTypeRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "simpleVehicleTypeRefs_RelStructure"

    simple_vehicle_type_ref: List[SimpleVehicleTypeRef] = field(
        default_factory=list,
        metadata={
            "name": "SimpleVehicleTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
