from dataclasses import dataclass
from .sales_transaction_frame_version_frame_structure import (
    SalesTransactionFrameVersionFrameStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SalesTransactionFrame(SalesTransactionFrameVersionFrameStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
