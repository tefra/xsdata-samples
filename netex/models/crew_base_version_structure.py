from dataclasses import dataclass, field
from typing import Optional, Union

from .garage_point_ref import GaragePointRef
from .garage_refs_rel_structure import GarageRefsRelStructure
from .group_of_entities_version_structure import (
    GroupOfEntitiesVersionStructure,
)
from .parking_point_ref import ParkingPointRef
from .relief_point_ref import ReliefPointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CrewBaseVersionStructure(GroupOfEntitiesVersionStructure):
    class Meta:
        name = "CrewBase_VersionStructure"

    parking_point_ref_or_relief_point_ref: GaragePointRef | ParkingPointRef | ReliefPointRef | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "GaragePointRef",
                    "type": GaragePointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPointRef",
                    "type": ParkingPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ReliefPointRef",
                    "type": ReliefPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    garages: GarageRefsRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
