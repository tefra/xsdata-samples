from dataclasses import dataclass
from .geographical_interval_price_versioned_child_structure import GeographicalIntervalPriceVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GeographicalIntervalPrice(GeographicalIntervalPriceVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
