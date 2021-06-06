from dataclasses import dataclass, field
from typing import List, Optional
from .garage_point_ref import GaragePointRef
from .garage_refs_rel_structure import GarageRefsRelStructure
from .group_of_entities_version_structure import GroupOfEntitiesVersionStructure
from .parking_point_ref import ParkingPointRef
from .relief_point_ref import ReliefPointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CrewBaseVersionStructure(GroupOfEntitiesVersionStructure):
    class Meta:
        name = "CrewBase_VersionStructure"

    garage_point_ref: List[GaragePointRef] = field(
        default_factory=list,
        metadata={
            "name": "GaragePointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 3,
            "sequential": True,
        }
    )
    parking_point_ref: List[ParkingPointRef] = field(
        default_factory=list,
        metadata={
            "name": "ParkingPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    relief_point_ref: Optional[ReliefPointRef] = field(
        default=None,
        metadata={
            "name": "ReliefPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    garages: Optional[GarageRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
