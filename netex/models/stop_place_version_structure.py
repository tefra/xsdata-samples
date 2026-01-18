from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .access_spaces_rel_structure import AccessSpacesRelStructure
from .accesses_rel_structure import AccessesRelStructure
from .air_submode import AirSubmode
from .all_vehicle_modes_of_transport_enumeration import (
    AllVehicleModesOfTransportEnumeration,
)
from .bus_submode import BusSubmode
from .coach_submode import CoachSubmode
from .explicit_equipments_rel_structure import ExplicitEquipmentsRelStructure
from .flexible_mode_of_operation_ref import FlexibleModeOfOperationRef
from .funicular_submode import FunicularSubmode
from .interchange_weighting_enumeration import InterchangeWeightingEnumeration
from .limited_use_type_enumeration import LimitedUseTypeEnumeration
from .metro_submode import MetroSubmode
from .navigation_paths_rel_structure import NavigationPathsRelStructure
from .path_junctions_rel_structure import PathJunctionsRelStructure
from .personal_mode_of_operation_ref import PersonalModeOfOperationRef
from .quays_rel_structure import QuaysRelStructure
from .rail_submode import RailSubmode
from .scheduled_mode_of_operation_ref import ScheduledModeOfOperationRef
from .site_path_links_rel_structure import SitePathLinksRelStructure
from .site_version_structure import SiteVersionStructure
from .snow_and_ice_submode import SnowAndIceSubmode
from .stop_place_weight_enumeration import StopPlaceWeightEnumeration
from .stop_type_enumeration import StopTypeEnumeration
from .tariff_zone_refs_rel_structure import TariffZoneRefsRelStructure
from .telecabin_submode import TelecabinSubmode
from .topographic_place_refs_rel_structure import (
    TopographicPlaceRefsRelStructure,
)
from .tram_submode import TramSubmode
from .vehicle_mode_enumeration import VehicleModeEnumeration
from .vehicle_pooling_ref import VehiclePoolingRef
from .vehicle_rental_ref import VehicleRentalRef
from .vehicle_sharing_ref import VehicleSharingRef
from .vehicle_stopping_places_rel_structure import (
    VehicleStoppingPlacesRelStructure,
)
from .water_submode import WaterSubmode

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StopPlaceVersionStructure(SiteVersionStructure):
    class Meta:
        name = "StopPlace_VersionStructure"

    public_code: None | str = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transport_mode: None | AllVehicleModesOfTransportEnumeration = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    choice_1: (
        None
        | AirSubmode
        | BusSubmode
        | CoachSubmode
        | FunicularSubmode
        | MetroSubmode
        | TramSubmode
        | TelecabinSubmode
        | RailSubmode
        | WaterSubmode
        | SnowAndIceSubmode
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AirSubmode",
                    "type": AirSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BusSubmode",
                    "type": BusSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CoachSubmode",
                    "type": CoachSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FunicularSubmode",
                    "type": FunicularSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MetroSubmode",
                    "type": MetroSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TramSubmode",
                    "type": TramSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TelecabinSubmode",
                    "type": TelecabinSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RailSubmode",
                    "type": RailSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WaterSubmode",
                    "type": WaterSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SnowAndIceSubmode",
                    "type": SnowAndIceSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    mode_of_operation_ref_or_alternative_mode_of_operation_ref_or_conventional_mode_of_operation_ref: (
        None
        | PersonalModeOfOperationRef
        | VehiclePoolingRef
        | VehicleSharingRef
        | VehicleRentalRef
        | FlexibleModeOfOperationRef
        | ScheduledModeOfOperationRef
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PersonalModeOfOperationRef",
                    "type": PersonalModeOfOperationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehiclePoolingRef",
                    "type": VehiclePoolingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingRef",
                    "type": VehicleSharingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleRentalRef",
                    "type": VehicleRentalRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleModeOfOperationRef",
                    "type": FlexibleModeOfOperationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ScheduledModeOfOperationRef",
                    "type": ScheduledModeOfOperationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    other_transport_modes: Iterable[VehicleModeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "OtherTransportModes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    tariff_zones: None | TariffZoneRefsRelStructure = field(
        default=None,
        metadata={
            "name": "tariffZones",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    stop_place_type: None | StopTypeEnumeration = field(
        default=None,
        metadata={
            "name": "StopPlaceType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    border_crossing: None | bool = field(
        default=None,
        metadata={
            "name": "BorderCrossing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    unlocalised_equipments: None | ExplicitEquipmentsRelStructure = field(
        default=None,
        metadata={
            "name": "unlocalisedEquipments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    served_places: None | TopographicPlaceRefsRelStructure = field(
        default=None,
        metadata={
            "name": "servedPlaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    main_terminus_for_places: None | TopographicPlaceRefsRelStructure = field(
        default=None,
        metadata={
            "name": "mainTerminusForPlaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    limited_use: None | LimitedUseTypeEnumeration = field(
        default=None,
        metadata={
            "name": "LimitedUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    weighting: None | InterchangeWeightingEnumeration = field(
        default=None,
        metadata={
            "name": "Weighting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    stop_place_weight: None | StopPlaceWeightEnumeration = field(
        default=None,
        metadata={
            "name": "StopPlaceWeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    quays: None | QuaysRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    access_spaces: None | AccessSpacesRelStructure = field(
        default=None,
        metadata={
            "name": "accessSpaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    path_links: None | SitePathLinksRelStructure = field(
        default=None,
        metadata={
            "name": "pathLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    path_junctions: None | PathJunctionsRelStructure = field(
        default=None,
        metadata={
            "name": "pathJunctions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accesses: None | AccessesRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    navigation_paths: None | NavigationPathsRelStructure = field(
        default=None,
        metadata={
            "name": "navigationPaths",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_stopping_places: None | VehicleStoppingPlacesRelStructure = field(
        default=None,
        metadata={
            "name": "vehicleStoppingPlaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
