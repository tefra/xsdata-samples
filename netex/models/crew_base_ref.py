from __future__ import annotations

from dataclasses import dataclass

from .crew_base_ref_structure import CrewBaseRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CrewBaseRef(CrewBaseRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
