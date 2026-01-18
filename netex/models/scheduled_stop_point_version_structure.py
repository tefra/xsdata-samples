from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional, Union

from .country_ref import CountryRef
from .external_object_ref_structure import ExternalObjectRefStructure
from .multilingual_string import MultilingualString
from .presentation_structure import PresentationStructure
from .private_code import PrivateCode
from .private_code_structure import PrivateCodeStructure
from .request_method_type_enumeration import RequestMethodTypeEnumeration
from .stop_area_refs_rel_structure import StopAreaRefsRelStructure
from .stop_type_enumeration import StopTypeEnumeration
from .tariff_zone_refs_rel_structure import TariffZoneRefsRelStructure
from .timing_point_version_structure import TimingPointVersionStructure
from .topographic_place_ref import TopographicPlaceRef
from .topographic_place_view import TopographicPlaceView
from .vehicle_mode_enumeration import VehicleModeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ScheduledStopPointVersionStructure(TimingPointVersionStructure):
    class Meta:
        name = "ScheduledStopPoint_VersionStructure"

    stop_areas: StopAreaRefsRelStructure | None = field(
        default=None,
        metadata={
            "name": "stopAreas",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tariff_zones: TariffZoneRefsRelStructure | None = field(
        default=None,
        metadata={
            "name": "tariffZones",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    short_name: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    name_suffix: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "NameSuffix",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    label: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    short_stop_code: PrivateCodeStructure | None = field(
        default=None,
        metadata={
            "name": "ShortStopCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    public_code: PrivateCodeStructure | None = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    private_code: PrivateCode | None = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    external_stop_point_ref: ExternalObjectRefStructure | None = field(
        default=None,
        metadata={
            "name": "ExternalStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    url: str | None = field(
        default=None,
        metadata={
            "name": "Url",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    stop_type: StopTypeEnumeration | None = field(
        default=None,
        metadata={
            "name": "StopType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    compass_bearing: float | None = field(
        default=None,
        metadata={
            "name": "CompassBearing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    presentation: PresentationStructure | None = field(
        default=None,
        metadata={
            "name": "Presentation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_modes: Iterable[VehicleModeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "VehicleModes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    for_alighting: bool | None = field(
        default=None,
        metadata={
            "name": "ForAlighting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    for_boarding: bool | None = field(
        default=None,
        metadata={
            "name": "ForBoarding",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    request_stop: bool | None = field(
        default=None,
        metadata={
            "name": "RequestStop",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    request_method_type: RequestMethodTypeEnumeration | None = field(
        default=None,
        metadata={
            "name": "RequestMethodType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    country_ref: CountryRef | None = field(
        default=None,
        metadata={
            "name": "CountryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    topographic_place_ref_or_topographic_place_view: TopographicPlaceRef | TopographicPlaceView | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TopographicPlaceRef",
                    "type": TopographicPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TopographicPlaceView",
                    "type": TopographicPlaceView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    at_centre: bool | None = field(
        default=None,
        metadata={
            "name": "AtCentre",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
