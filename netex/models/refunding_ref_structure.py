from __future__ import annotations

from dataclasses import dataclass

from .reselling_ref_structure import ResellingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RefundingRefStructure(ResellingRefStructure):
    pass
