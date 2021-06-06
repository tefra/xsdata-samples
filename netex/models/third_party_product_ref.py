from dataclasses import dataclass
from .third_party_product_ref_structure import ThirdPartyProductRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ThirdPartyProductRef(ThirdPartyProductRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
