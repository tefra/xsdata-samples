from __future__ import annotations

from dataclasses import dataclass

from .entitlement_required_version_structure import (
    EntitlementRequiredVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EntitlementRequired(EntitlementRequiredVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
