from dataclasses import dataclass, field
from typing import Optional

from .all_vehicle_modes_of_transport_enumeration import (
    AllVehicleModesOfTransportEnumeration,
)
from .alternative_names_rel_structure import AlternativeNamesRelStructure
from .flexible_stop_place_ref import FlexibleStopPlaceRef
from .multilingual_string import MultilingualString
from .place_version_structure import PlaceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FlexibleQuayVersionStructure(PlaceVersionStructure):
    class Meta:
        name = "FlexibleQuay_VersionStructure"

    name_suffix: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "NameSuffix",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    alternative_names: Optional[AlternativeNamesRelStructure] = field(
        default=None,
        metadata={
            "name": "alternativeNames",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    flexible_stop_place_ref: Optional[FlexibleStopPlaceRef] = field(
        default=None,
        metadata={
            "name": "FlexibleStopPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transport_mode: Optional[AllVehicleModesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    boarding_use: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BoardingUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    alighting_use: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AlightingUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    public_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
