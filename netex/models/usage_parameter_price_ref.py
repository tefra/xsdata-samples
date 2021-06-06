from dataclasses import dataclass
from .usage_parameter_price_ref_structure import UsageParameterPriceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class UsageParameterPriceRef(UsageParameterPriceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
