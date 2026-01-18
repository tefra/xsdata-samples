from __future__ import annotations

from dataclasses import dataclass

from .entity_in_version_structure import VersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerEligibility2(VersionedChildStructure):
    class Meta:
        name = "CustomerEligibility_"
        namespace = "http://www.netex.org.uk/netex"
