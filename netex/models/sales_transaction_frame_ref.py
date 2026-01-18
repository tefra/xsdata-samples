from __future__ import annotations

from dataclasses import dataclass

from .sales_transaction_frame_ref_structure import (
    SalesTransactionFrameRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SalesTransactionFrameRef(SalesTransactionFrameRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
