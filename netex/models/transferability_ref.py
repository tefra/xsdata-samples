from __future__ import annotations

from dataclasses import dataclass

from .transferability_ref_structure import TransferabilityRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TransferabilityRef(TransferabilityRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
