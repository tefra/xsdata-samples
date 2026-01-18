from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

from .fare_unit_version_structure import FareUnitVersionStructure
from .time_unit_prices_rel_structure import TimeUnitPricesRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimeUnitVersionStructure(FareUnitVersionStructure):
    class Meta:
        name = "TimeUnit_VersionStructure"

    type_value: None | str = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    duration: None | XmlDuration = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    prices: None | TimeUnitPricesRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
