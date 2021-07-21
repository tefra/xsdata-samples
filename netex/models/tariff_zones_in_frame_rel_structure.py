from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .fare_zone import FareZone
from .tariff_zone_1 import TariffZone1
from .tariff_zone_2 import TariffZone2

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TariffZonesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "tariffZonesInFrame_RelStructure"

    fare_zone: List[FareZone] = field(
        default_factory=list,
        metadata={
            "name": "FareZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    tariff_zone: List[TariffZone1] = field(
        default_factory=list,
        metadata={
            "name": "TariffZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_tariff_zone: List[TariffZone2] = field(
        default_factory=list,
        metadata={
            "name": "TariffZone_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
