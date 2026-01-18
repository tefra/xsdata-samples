from __future__ import annotations

from dataclasses import dataclass

from .entitlement_given_ref_structure import EntitlementGivenRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EntitlementGivenRef(EntitlementGivenRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
