from dataclasses import dataclass, field
from typing import List, Optional
from netex.models.access_spaces_rel_structure import AccessSpacesRelStructure
from netex.models.accesses_rel_structure import AccessesRelStructure
from netex.models.air_submode_enumeration import AirSubmodeEnumeration
from netex.models.bus_submode_enumeration import BusSubmodeEnumeration
from netex.models.coach_submode_enumeration import CoachSubmodeEnumeration
from netex.models.explicit_equipments_rel_structure import ExplicitEquipmentsRelStructure
from netex.models.funicular_submode_enumeration import FunicularSubmodeEnumeration
from netex.models.interchange_weighting_enumeration import InterchangeWeightingEnumeration
from netex.models.limited_use_type_enumeration import LimitedUseTypeEnumeration
from netex.models.metro_submode_enumeration import MetroSubmodeEnumeration
from netex.models.navigation_paths_rel_structure import NavigationPathsRelStructure
from netex.models.path_junctions_rel_structure import PathJunctionsRelStructure
from netex.models.quays_rel_structure import QuaysRelStructure
from netex.models.rail_submode_enumeration import RailSubmodeEnumeration
from netex.models.site_path_links_rel_structure import SitePathLinksRelStructure
from netex.models.site_version_structure import SiteVersionStructure
from netex.models.snow_and_ice_submode_enumeration import SnowAndIceSubmodeEnumeration
from netex.models.stop_place_weight_enumeration import StopPlaceWeightEnumeration
from netex.models.stop_type_enumeration import StopTypeEnumeration
from netex.models.tariff_zone_refs_rel_structure import TariffZoneRefsRelStructure
from netex.models.telecabin_submode_enumeration import TelecabinSubmodeEnumeration
from netex.models.topographic_place_refs_rel_structure import TopographicPlaceRefsRelStructure
from netex.models.tram_submode_enumeration import TramSubmodeEnumeration
from netex.models.vehicle_mode_enumeration import VehicleModeEnumeration
from netex.models.vehicle_stopping_places_rel_structure import VehicleStoppingPlacesRelStructure
from netex.models.water_submode_enumeration import WaterSubmodeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StopPlaceVersionStructure(SiteVersionStructure):
    class Meta:
        name = "StopPlace_VersionStructure"

    public_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PublicCode",
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
    air_submode: Optional[AirSubmodeEnumeration] = field(
        default=None,
        metadata={
            "name": "AirSubmode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    bus_submode: Optional[BusSubmodeEnumeration] = field(
        default=None,
        metadata={
            "name": "BusSubmode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    coach_submode: Optional[CoachSubmodeEnumeration] = field(
        default=None,
        metadata={
            "name": "CoachSubmode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    funicular_submode: Optional[FunicularSubmodeEnumeration] = field(
        default=None,
        metadata={
            "name": "FunicularSubmode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    metro_submode: Optional[MetroSubmodeEnumeration] = field(
        default=None,
        metadata={
            "name": "MetroSubmode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    tram_submode: Optional[TramSubmodeEnumeration] = field(
        default=None,
        metadata={
            "name": "TramSubmode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    telecabin_submode: Optional[TelecabinSubmodeEnumeration] = field(
        default=None,
        metadata={
            "name": "TelecabinSubmode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    rail_submode: Optional[RailSubmodeEnumeration] = field(
        default=None,
        metadata={
            "name": "RailSubmode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    water_submode: Optional[WaterSubmodeEnumeration] = field(
        default=None,
        metadata={
            "name": "WaterSubmode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    snow_and_ice_submode: Optional[SnowAndIceSubmodeEnumeration] = field(
        default=None,
        metadata={
            "name": "SnowAndIceSubmode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    other_transport_modes: List[VehicleModeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "OtherTransportModes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    tariff_zones: Optional[TariffZoneRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "tariffZones",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_place_type: Optional[StopTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "StopPlaceType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    border_crossing: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BorderCrossing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    unlocalised_equipments: Optional[ExplicitEquipmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "unlocalisedEquipments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    served_places: Optional[TopographicPlaceRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "servedPlaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    main_terminus_for_places: Optional[TopographicPlaceRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "mainTerminusForPlaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    limited_use: Optional[LimitedUseTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "LimitedUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    weighting: Optional[InterchangeWeightingEnumeration] = field(
        default=None,
        metadata={
            "name": "Weighting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_place_weight: Optional[StopPlaceWeightEnumeration] = field(
        default=None,
        metadata={
            "name": "StopPlaceWeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    quays: Optional[QuaysRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    access_spaces: Optional[AccessSpacesRelStructure] = field(
        default=None,
        metadata={
            "name": "accessSpaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    path_links: Optional[SitePathLinksRelStructure] = field(
        default=None,
        metadata={
            "name": "pathLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    path_junctions: Optional[PathJunctionsRelStructure] = field(
        default=None,
        metadata={
            "name": "pathJunctions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    accesses: Optional[AccessesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    navigation_paths: Optional[NavigationPathsRelStructure] = field(
        default=None,
        metadata={
            "name": "navigationPaths",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_stopping_places: Optional[VehicleStoppingPlacesRelStructure] = field(
        default=None,
        metadata={
            "name": "vehicleStoppingPlaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
