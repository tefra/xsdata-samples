from dataclasses import dataclass, field
from typing import List, Optional
from .alternative_names_rel_structure import AlternativeNamesRelStructure
from .flexible_area import FlexibleArea
from .flexible_area_ref import FlexibleAreaRef
from .hail_and_ride_area import HailAndRideArea
from .hail_and_ride_area_ref import HailAndRideAreaRef
from .line_refs_rel_structure import LineRefsRelStructure
from .multilingual_string import MultilingualString
from .place_version_structure import PlaceVersionStructure
from .vehicle_mode_enumeration import VehicleModeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FlexibleStopPlaceVersionStructure(PlaceVersionStructure):
    class Meta:
        name = "FlexibleStopPlace_VersionStructure"

    name_suffix: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "NameSuffix",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    alternative_names: Optional[AlternativeNamesRelStructure] = field(
        default=None,
        metadata={
            "name": "alternativeNames",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transport_mode: Optional[VehicleModeEnumeration] = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    public_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    areas: Optional["FlexibleStopPlaceVersionStructure.Areas"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    lines: Optional[LineRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )

    @dataclass
    class Areas:
        flexible_area: List[FlexibleArea] = field(
            default_factory=list,
            metadata={
                "name": "FlexibleArea",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        flexible_area_ref: List[FlexibleAreaRef] = field(
            default_factory=list,
            metadata={
                "name": "FlexibleAreaRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        hail_and_ride_area: List[HailAndRideArea] = field(
            default_factory=list,
            metadata={
                "name": "HailAndRideArea",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        hail_and_ride_area_ref: List[HailAndRideAreaRef] = field(
            default_factory=list,
            metadata={
                "name": "HailAndRideAreaRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
