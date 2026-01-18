from __future__ import annotations

from dataclasses import dataclass

from .transfer_ref_structure import TransferRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessRefStructure(TransferRefStructure):
    pass
