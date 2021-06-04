from dataclasses import dataclass, field
from typing import Optional
from netex.models.air_submode_enumeration import AirSubmodeEnumeration
from netex.models.alternative_names_rel_structure import AlternativeNamesRelStructure
from netex.models.bus_submode_enumeration import BusSubmodeEnumeration
from netex.models.coach_submode_enumeration import CoachSubmodeEnumeration
from netex.models.funicular_submode_enumeration import FunicularSubmodeEnumeration
from netex.models.group_of_entities_version_structure import GroupOfEntitiesVersionStructure
from netex.models.metro_submode_enumeration import MetroSubmodeEnumeration
from netex.models.polygon import Polygon
from netex.models.rail_submode_enumeration import RailSubmodeEnumeration
from netex.models.simple_point_version_structure import SimplePointVersionStructure
from netex.models.snow_and_ice_submode_enumeration import SnowAndIceSubmodeEnumeration
from netex.models.stop_place_refs_rel_structure import StopPlaceRefsRelStructure
from netex.models.telecabin_submode_enumeration import TelecabinSubmodeEnumeration
from netex.models.tram_submode_enumeration import TramSubmodeEnumeration
from netex.models.vehicle_mode_enumeration import VehicleModeEnumeration
from netex.models.water_submode_enumeration import WaterSubmodeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfStopPlacesStructure(GroupOfEntitiesVersionStructure):
    public_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    members: Optional[StopPlaceRefsRelStructure] = field(
        default=None,
        metadata={
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
    centroid: Optional[SimplePointVersionStructure] = field(
        default=None,
        metadata={
            "name": "Centroid",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    polygon: Optional[Polygon] = field(
        default=None,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
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
