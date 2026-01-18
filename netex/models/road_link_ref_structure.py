from __future__ import annotations

from dataclasses import dataclass

from .infrastructure_link_ref_structure import InfrastructureLinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoadLinkRefStructure(InfrastructureLinkRefStructure):
    pass
