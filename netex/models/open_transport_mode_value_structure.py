from dataclasses import dataclass, field
from typing import Optional, Union
from .air_submode_enumeration import AirSubmodeEnumeration
from .all_modes_enumeration import AllModesEnumeration
from .bus_submode_enumeration import BusSubmodeEnumeration
from .coach_submode_enumeration import CoachSubmodeEnumeration
from .funicular_submode_enumeration import FunicularSubmodeEnumeration
from .metro_submode_enumeration import MetroSubmodeEnumeration
from .rail_submode_enumeration import RailSubmodeEnumeration
from .self_drive_submode_enumeration import SelfDriveSubmodeEnumeration
from .snow_and_ice_submode_enumeration import SnowAndIceSubmodeEnumeration
from .submode_ref import SubmodeRef
from .taxi_submode_enumeration import TaxiSubmodeEnumeration
from .telecabin_submode_enumeration import TelecabinSubmodeEnumeration
from .tram_submode_enumeration import TramSubmodeEnumeration
from .type_of_value_version_structure import TypeOfValueVersionStructure
from .water_submode_enumeration import WaterSubmodeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OpenTransportModeValueStructure(TypeOfValueVersionStructure):
    class Meta:
        name = "OpenTransportMode_ValueStructure"

    transport_mode: Optional[AllModesEnumeration] = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    choice: Optional[Union[AirSubmodeEnumeration, BusSubmodeEnumeration, CoachSubmodeEnumeration, FunicularSubmodeEnumeration, MetroSubmodeEnumeration, TramSubmodeEnumeration, TelecabinSubmodeEnumeration, RailSubmodeEnumeration, WaterSubmodeEnumeration, SnowAndIceSubmodeEnumeration, TaxiSubmodeEnumeration, SelfDriveSubmodeEnumeration]] = field(
        default=None,
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
                {
                    "name": "TaxiSubmode",
                    "type": TaxiSubmodeEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SelfDriveSubmode",
                    "type": SelfDriveSubmodeEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    submode_ref: Optional[SubmodeRef] = field(
        default=None,
        metadata={
            "name": "SubmodeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
