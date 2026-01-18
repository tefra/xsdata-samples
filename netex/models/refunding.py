from __future__ import annotations

from dataclasses import dataclass

from .refunding_version_structure import RefundingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Refunding(RefundingVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
