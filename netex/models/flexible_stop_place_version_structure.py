from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional, Union

from .all_vehicle_modes_of_transport_enumeration import (
    AllVehicleModesOfTransportEnumeration,
)
from .alternative_names_rel_structure import AlternativeNamesRelStructure
from .flexible_area import FlexibleArea
from .flexible_area_ref import FlexibleAreaRef
from .hail_and_ride_area import HailAndRideArea
from .hail_and_ride_area_ref import HailAndRideAreaRef
from .line_refs_rel_structure import LineRefsRelStructure
from .multilingual_string import MultilingualString
from .place_version_structure import PlaceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FlexibleStopPlaceVersionStructure(PlaceVersionStructure):
    class Meta:
        name = "FlexibleStopPlace_VersionStructure"

    name_suffix: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "NameSuffix",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    alternative_names: AlternativeNamesRelStructure | None = field(
        default=None,
        metadata={
            "name": "alternativeNames",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transport_mode: AllVehicleModesOfTransportEnumeration | None = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    public_code: str | None = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    areas: FlexibleStopPlaceVersionStructure.Areas | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    lines: LineRefsRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )

    @dataclass
    class Areas:
        choice: Iterable[
            FlexibleArea | FlexibleAreaRef | HailAndRideArea | HailAndRideAreaRef
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
