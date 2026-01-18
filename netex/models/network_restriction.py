from __future__ import annotations

from dataclasses import dataclass

from .network_restriction_version_structure import (
    NetworkRestrictionVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class NetworkRestriction(NetworkRestrictionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
