from __future__ import annotations

from dataclasses import dataclass

from .transfer_version_structure import TransferVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Transfer(TransferVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
