from __future__ import annotations

from dataclasses import dataclass

from .link_version_structure import LinkVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InfrastructureLinkVersionStructure(LinkVersionStructure):
    class Meta:
        name = "InfrastructureLink_VersionStructure"
