from dataclasses import dataclass, field
from typing import Optional
from netex.models.air_submode_enumeration import AirSubmodeEnumeration
from netex.models.all_modes_enumeration import AllModesEnumeration
from netex.models.bus_submode_enumeration import BusSubmodeEnumeration
from netex.models.coach_submode_enumeration import CoachSubmodeEnumeration
from netex.models.funicular_submode_enumeration import FunicularSubmodeEnumeration
from netex.models.metro_submode_enumeration import MetroSubmodeEnumeration
from netex.models.rail_submode_enumeration import RailSubmodeEnumeration
from netex.models.self_drive_submode_enumeration import SelfDriveSubmodeEnumeration
from netex.models.snow_and_ice_submode_enumeration import SnowAndIceSubmodeEnumeration
from netex.models.submode_ref import SubmodeRef
from netex.models.taxi_submode_enumeration import TaxiSubmodeEnumeration
from netex.models.telecabin_submode_enumeration import TelecabinSubmodeEnumeration
from netex.models.tram_submode_enumeration import TramSubmodeEnumeration
from netex.models.type_of_value_version_structure import TypeOfValueVersionStructure
from netex.models.water_submode_enumeration import WaterSubmodeEnumeration

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
    taxi_submode: Optional[TaxiSubmodeEnumeration] = field(
        default=None,
        metadata={
            "name": "TaxiSubmode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    self_drive_submode: Optional[SelfDriveSubmodeEnumeration] = field(
        default=None,
        metadata={
            "name": "SelfDriveSubmode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
