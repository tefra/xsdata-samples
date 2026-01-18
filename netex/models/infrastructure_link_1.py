from __future__ import annotations

from dataclasses import dataclass

from .infrastructure_link_version_structure import (
    InfrastructureLinkVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InfrastructureLink1(InfrastructureLinkVersionStructure):
    class Meta:
        name = "InfrastructureLink"
        namespace = "http://www.netex.org.uk/netex"
