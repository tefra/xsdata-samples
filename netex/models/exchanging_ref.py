from dataclasses import dataclass
from .exchanging_ref_structure import ExchangingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ExchangingRef(ExchangingRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
