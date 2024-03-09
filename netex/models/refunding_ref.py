from dataclasses import dataclass

from .refunding_ref_structure import RefundingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RefundingRef(RefundingRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
