from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from netex.models.fare_interval_version_structure import FareIntervalVersionStructure
from netex.models.geographical_interval_prices_rel_structure import GeographicalIntervalPricesRelStructure
from netex.models.geographical_unit_ref import GeographicalUnitRef
from netex.models.interval_type_enumeration import IntervalTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GeographicalIntervalVersionStructure(FareIntervalVersionStructure):
    class Meta:
        name = "GeographicalInterval_VersionStructure"

    start_geographical_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "StartGeographicalValue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_geographical_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "EndGeographicalValue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    number_of_units: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfUnits",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    interval_type: Optional[IntervalTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "IntervalType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    geographical_unit_ref: Optional[GeographicalUnitRef] = field(
        default=None,
        metadata={
            "name": "GeographicalUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    prices: Optional[GeographicalIntervalPricesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
