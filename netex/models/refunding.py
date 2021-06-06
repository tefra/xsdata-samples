from dataclasses import dataclass
from .refunding_version_structure import RefundingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Refunding(RefundingVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
