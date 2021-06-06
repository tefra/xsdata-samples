from dataclasses import dataclass
from .purchase_window_ref_structure import PurchaseWindowRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PurchaseWindowRef(PurchaseWindowRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
