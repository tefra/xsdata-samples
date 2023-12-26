from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from .fare_unit_version_structure import FareUnitVersionStructure
from .time_unit_prices_rel_structure import TimeUnitPricesRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TimeUnitVersionStructure(FareUnitVersionStructure):
    class Meta:
        name = "TimeUnit_VersionStructure"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    prices: Optional[TimeUnitPricesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
