from dataclasses import dataclass
from netex.models.sales_transaction_ref_structure import SalesTransactionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SalesTransactionRef(SalesTransactionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
