from dataclasses import dataclass
from .usage_parameter_price_versioned_child_structure import (
    UsageParameterPriceVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class UsageParameterPrice(UsageParameterPriceVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
