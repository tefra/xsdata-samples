from __future__ import annotations

from dataclasses import dataclass, field

from .address_version_structure import AddressVersionStructure
from .compass_bearing16_enumeration import CompassBearing16Enumeration
from .multilingual_string import MultilingualString
from .road_number_range_structure import RoadNumberRangeStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RoadAddressVersionStructure(AddressVersionStructure):
    class Meta:
        name = "RoadAddress_VersionStructure"

    gis_feature_ref: str | None = field(
        default=None,
        metadata={
            "name": "GisFeatureRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    road_number: str | None = field(
        default=None,
        metadata={
            "name": "RoadNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    road_name: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "RoadName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    bearing_compass: CompassBearing16Enumeration | None = field(
        default=None,
        metadata={
            "name": "BearingCompass",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    bearing_degrees: int | None = field(
        default=None,
        metadata={
            "name": "BearingDegrees",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    odd_number_range: RoadNumberRangeStructure | None = field(
        default=None,
        metadata={
            "name": "OddNumberRange",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    even_number_range: RoadNumberRangeStructure | None = field(
        default=None,
        metadata={
            "name": "EvenNumberRange",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
