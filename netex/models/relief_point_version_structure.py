from dataclasses import dataclass, field
from typing import Optional

from .crew_base_ref import CrewBaseRef
from .timing_point_version_structure import TimingPointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ReliefPointVersionStructure(TimingPointVersionStructure):
    class Meta:
        name = "ReliefPoint_VersionStructure"

    crew_base_ref: Optional[CrewBaseRef] = field(
        default=None,
        metadata={
            "name": "CrewBaseRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
