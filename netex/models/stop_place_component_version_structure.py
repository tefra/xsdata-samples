from dataclasses import dataclass, field
from typing import List, Optional
from .air_submode_enumeration import AirSubmodeEnumeration
from .bus_submode_enumeration import BusSubmodeEnumeration
from .coach_submode_enumeration import CoachSubmodeEnumeration
from .funicular_submode_enumeration import FunicularSubmodeEnumeration
from .metro_submode_enumeration import MetroSubmodeEnumeration
from .rail_submode_enumeration import RailSubmodeEnumeration
from .site_component_version_structure import SiteComponentVersionStructure
from .snow_and_ice_submode_enumeration import SnowAndIceSubmodeEnumeration
from .tariff_zone_refs_rel_structure import TariffZoneRefsRelStructure
from .telecabin_submode_enumeration import TelecabinSubmodeEnumeration
from .tram_submode_enumeration import TramSubmodeEnumeration
from .vehicle_mode_enumeration import VehicleModeEnumeration
from .water_submode_enumeration import WaterSubmodeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StopPlaceComponentVersionStructure(SiteComponentVersionStructure):
    class Meta:
        name = "StopPlaceComponent_VersionStructure"

    transport_mode: Optional[VehicleModeEnumeration] = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AirSubmode",
                    "type": AirSubmodeEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BusSubmode",
                    "type": BusSubmodeEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CoachSubmode",
                    "type": CoachSubmodeEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FunicularSubmode",
                    "type": FunicularSubmodeEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MetroSubmode",
                    "type": MetroSubmodeEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TramSubmode",
                    "type": TramSubmodeEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TelecabinSubmode",
                    "type": TelecabinSubmodeEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RailSubmode",
                    "type": RailSubmodeEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WaterSubmode",
                    "type": WaterSubmodeEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SnowAndIceSubmode",
                    "type": SnowAndIceSubmodeEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 10,
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
