from __future__ import annotations

from dataclasses import dataclass

from .crew_base_version_structure import CrewBaseVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CrewBase(CrewBaseVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
