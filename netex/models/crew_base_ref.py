from dataclasses import dataclass
from netex.models.crew_base_ref_structure import CrewBaseRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CrewBaseRef(CrewBaseRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
