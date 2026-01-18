from __future__ import annotations

from dataclasses import dataclass

from .infrastructure_link_restriction_version_structure import (
    InfrastructureLinkRestrictionVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InfrastructureLinkRestriction(
    InfrastructureLinkRestrictionVersionStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
