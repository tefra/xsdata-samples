from dataclasses import dataclass, field
from typing import List, Optional, Union
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
    transport_mode: Optional[VehicleModeEnumeration] = field(
        default=None,
        metadata={
            "name": "TransportMode",
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
    areas: Optional["FlexibleStopPlaceVersionStructure.Areas"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    lines: Optional[LineRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )

    @dataclass
    class Areas:
        choice: List[
            Union[
                FlexibleArea,
                FlexibleAreaRef,
                HailAndRideArea,
                HailAndRideAreaRef,
            ]
        ] = field(
            default_factory=list,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "FlexibleArea",
                        "type": FlexibleArea,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "FlexibleAreaRef",
                        "type": FlexibleAreaRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "HailAndRideArea",
                        "type": HailAndRideArea,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "HailAndRideAreaRef",
                        "type": HailAndRideAreaRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                ),
            },
        )
