from __future__ import annotations

from dataclasses import dataclass

from .transfer_restriction_ref_structure import TransferRestrictionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TransferRestrictionRef(TransferRestrictionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
