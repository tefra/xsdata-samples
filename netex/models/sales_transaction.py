from dataclasses import dataclass
from .sales_transaction_version_structure import (
    SalesTransactionVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SalesTransaction(SalesTransactionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
