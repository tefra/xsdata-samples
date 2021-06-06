from dataclasses import dataclass, field
from typing import Optional
from .air_submode_enumeration import AirSubmodeEnumeration
from .bus_submode_enumeration import BusSubmodeEnumeration
from .coach_submode_enumeration import CoachSubmodeEnumeration
from .funicular_submode_enumeration import FunicularSubmodeEnumeration
from .metro_submode_enumeration import MetroSubmodeEnumeration
from .rail_submode_enumeration import RailSubmodeEnumeration
from .snow_and_ice_submode_enumeration import SnowAndIceSubmodeEnumeration
from .telecabin_submode_enumeration import TelecabinSubmodeEnumeration
from .tram_submode_enumeration import TramSubmodeEnumeration
from .water_submode_enumeration import WaterSubmodeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TransportSubmodeStructure:
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
