from dataclasses import dataclass
from netex.models.time_interval_price_ref_structure import TimeIntervalPriceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimeIntervalPriceRef(TimeIntervalPriceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
